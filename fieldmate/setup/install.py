# fieldmate/setup/install.py

import frappe
from frappe import _

REQUIRED_APPS = {"frappe", "erpnext", "builder"}

def before_app_install(app_name):
    missing = [app for app in REQUIRED_APPS if app not in frappe.get_installed_apps()]
    if missing:
        msg = _("Cannot install Fieldmate: required apps are missing: {0}").format(", ".join(missing))
        frappe.throw(msg, title=_("Missing Dependencies"))

def after_app_install(app_name):
    from fieldmate.setup.custom_fields import setup_custom_fields
    setup_custom_fields()
