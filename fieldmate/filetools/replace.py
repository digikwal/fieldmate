# fieldmate/filetools/replace.py
import os
import hashlib
import frappe
from frappe.utils import cint

WEBSITE_FOLDER = "Home/Website"  # strict, case-sensitive

# ---------- helpers ----------

def _abs_path_from_url(file_url: str) -> str:
    site_path = frappe.get_site_path()
    if file_url.startswith("/private/files/"):
        return os.path.join(site_path, file_url.lstrip("/"))  # sites/site/private/files/...
    # public
    return os.path.join(site_path, "public", file_url.lstrip("/"))  # sites/site/public/files/...

def _compute_md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()

def _update_file_doc_metadata(file_doc, data: bytes):
    file_doc.content_hash = _compute_md5(data)
    file_doc.file_size = len(data)
    file_doc.save(ignore_permissions=True)

def _in_website_folder(folder: str) -> bool:
    if not folder:
        return False
    # exact match OR nested (e.g. "Home/Website/assets")
    return folder == WEBSITE_FOLDER or folder.startswith(WEBSITE_FOLDER + "/")

def _clear_website_cache():
    try:
        frappe.clear_cache()
        frappe.clear_cache(doctype="Website Settings")
    except Exception:
        pass

# ---------- main hook ----------

def on_file_after_insert(doc, method=None):
    """Replace existing public asset bytes at /files/<original_name> when:
       - user ticked x_fileReplace,
       - this File is public,
       - it lives in (or under) WEBSITE_FOLDER,
       - a File with the target URL already exists.
    """
    # preconditions
    if not cint(getattr(doc, "x_fileReplace", 0)):
        return
    if doc.is_private:
        return
    if not _in_website_folder(getattr(doc, "folder", "")):
        return
    if not doc.file_url or not doc.file_name:
        return

    # intended target name = what the user *meant* to replace
    target_name = (doc.get("original_file_name") or doc.file_name).strip()
    target_url = f"/files/{target_name}"

    # if upload already landed exactly at target (no suffix), nothing to do
    if doc.file_url == target_url:
        return

    # there must be an existing File that owns the canonical URL
    exists = frappe.db.get_value(
        "File",
        {"file_url": target_url, "is_private": 0},
        ["name", "file_url"],
        as_dict=True,
    )
    if not exists:
        # nothing to replace; keep new upload as-is
        return

    # read the just-uploaded bytes (source)
    src_path = _abs_path_from_url(doc.file_url)
    if not os.path.exists(src_path):
        return

    with open(src_path, "rb") as fh:
        new_data = fh.read()
    new_hash = _compute_md5(new_data)

    # load existing File doc & short-circuit if content is identical
    existing_doc = frappe.get_doc("File", exists["name"])
    if existing_doc.content_hash and existing_doc.content_hash == new_hash:
        # identical content: just delete the temporary upload
        _safe_delete_temp_upload(doc, src_path)
        return

    # overwrite the destination on disk
    dest_path = _abs_path_from_url(target_url)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "wb") as fh:
        fh.write(new_data)

    # update metadata on the existing File doc
    _update_file_doc_metadata(existing_doc, new_data)

    # clear website caches/CDN (CDN purge is user responsibility)
    _clear_website_cache()

    # remove the temporary “suffix” upload (doc + file on disk)
    _safe_delete_temp_upload(doc, src_path)

# ---------- cleanup ----------

def _safe_delete_temp_upload(temp_doc, src_path: str):
    """Delete the uploaded temp file (both disk + doc) without touching the destination."""
    try:
        if os.path.exists(src_path):
            os.remove(src_path)
    finally:
        # prevent File.delete() from trying to delete from disk again
        temp_doc.flags.ignore_permissions = True
        temp_doc.file_url = None
        try:
            temp_doc.delete()
        except Exception:
            # as a fallback, hard delete if needed
            frappe.db.delete("File", {"name": temp_doc.name})
            frappe.db.commit()
