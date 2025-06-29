import frappe
import os
import json
from pathlib import Path

EXCLUDED_KEYS = ["name", "creation", "modified", "owner", "modified_by", "idx"]
EXPORT_DIR = Path(frappe.get_app_path("fieldmate")) / "custom_field"

def export_fieldmate_fields(doc=None, method=None, verbose=False):
    """
    Export all Custom Fields with x_fieldmate=1 to JSON files.
    If triggered via hook (on_update/on_trash), only export the current field if x_fieldmate=1.
    """
    # Quick guard: skip if not a relevant x_fieldmate field
    if doc and not getattr(doc, "x_fieldmate", False):
        return

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    exported_files = set()

    # If called with a doc (e.g. via hook), export only that one field
    if doc:
        custom_fields = [{
            "name": doc.name,
            "dt": doc.dt,
            "fieldname": doc.fieldname
        }]
    else:
        # Full export (e.g. via CLI)
        custom_fields = get_fieldmate_custom_fields()

    for cf in custom_fields:
        filename = build_filename(cf["dt"], cf["fieldname"])
        file_path = EXPORT_DIR / filename
        exported_files.add(filename)

        doc_data = get_sanitized_field_data(cf["name"])

        if file_path.exists() and read_json(file_path) == doc_data:
            continue  # No change

        write_json(file_path, doc_data)
        log(f"Exported: {filename}", verbose)

    if not doc:
        # Only in full export: remove obsolete files
        cleanup_obsolete_files(exported_files, verbose)


# ──────────────── Helper Functions ────────────────

def get_fieldmate_custom_fields():
    return frappe.get_all(
        "Custom Field",
        filters={"x_fieldmate": 1},
        fields=["name", "dt", "fieldname"]
    )

def get_sanitized_field_data(name):
    doc = frappe.get_doc("Custom Field", name)
    return sanitize_field_data(doc.as_dict())

def build_filename(doctype, fieldname):
    return f"{doctype}--{fieldname}.json".replace(" ", "_")

def read_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def write_json(path: Path, data: dict):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True, default=str)

def cleanup_obsolete_files(valid_filenames: set, verbose: bool):
    all_files = {f.name for f in EXPORT_DIR.glob("*.json")}
    obsolete = all_files - valid_filenames

    for filename in obsolete:
        path = EXPORT_DIR / filename
        path.unlink()
        log(f"Deleted: {filename}", verbose)
        os.system(f"git rm --quiet --cached '{path}' || true")

def sanitize_field_data(data: dict) -> dict:
    """Remove system metadata fields from exported field definition."""
    return {k: v for k, v in data.items() if k not in EXCLUDED_KEYS}

def log(message: str, verbose: bool = False):
    if verbose:
        print(message)
    else:
        frappe.logger("fieldmate").info(message)
