import frappe
from frappe import _

REQUIRED_APPS = {"frappe", "erpnext", "builder"}

def before_app_install(app_name):
    missing = [app for app in REQUIRED_APPS if app not in frappe.get_installed_apps()]
    if missing:
        msg = _("Cannot install Fieldmate: required apps are missing: {0}").format(", ".join(missing))
        frappe.throw(msg, title=_("Missing Dependencies"))

def after_app_install(app_name):
    ensure_website_folder()
    from fieldmate.setup.custom_fields import setup_custom_fields
    setup_custom_fields()

def ensure_website_folder():
    """Create the public folder 'Home/Website' if it doesn't exist (case-sensitive, public)."""
    parent = "Home"
    name = "Website"

    # Already there?
    exists = frappe.db.exists("File", {
        "is_folder": 1,
        "file_name": name,
        "folder": parent,
        "is_private": 0
    })
    if exists:
        return

    # Prefer the framework helper if available
    try:
        from frappe.utils.file_manager import create_folder
        # create_folder(child_name, parent_name) is idempotent; it will no-op if it already exists
        create_folder(name, parent)
        return
    except Exception:
        # Fall back to manual insert (works across versions)
        pass

    doc = frappe.get_doc({
        "doctype": "File",
        "file_name": name,
        "is_folder": 1,
        "folder": parent,
        "is_private": 0
    })
    doc.insert(ignore_permissions=True)
