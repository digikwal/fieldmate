import frappe
from copy import deepcopy
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def setup_custom_fields():
    ensure_fieldmate_flag_exists()

    field_templates = {
        "x_coc": {
            "fieldname": "x_coc",
            "label": "Chamber of Commerce No.",
            "fieldtype": "Data",
            "insert_after": "tax_id",
            "unique": 1,
            "x_fieldmate": 1,
            "doctypes": ["Customer", "Supplier"]
        },
        "x_sbi": {
            "fieldname": "x_sbi",
            "label": "SBI Code",
            "fieldtype": "Data",
            "insert_after": "x_coc",
            "x_fieldmate": 1,
            "doctypes": ["Customer", "Supplier", "Company"]
        },
        "x_ai": {
            "fieldname": "x_ai",
            "label": "Allow AI Calls",
            "fieldtype": "Check",
            "insert_before": "job_title",
            "x_fieldmate": 1,
            "doctypes": ["Lead"]
        }
    }

    doctype_overrides = {
        "Company": {
            "x_coc": {
                "insert_after": "default_holiday_list"
            }
        }
    }

    target_doctypes = list({dt for f in field_templates.values() for dt in f["doctypes"]})
    fields = {dt: [] for dt in target_doctypes}

    for fieldname, base_def in field_templates.items():
        for dt in base_def.get("doctypes", []):
            field_def = deepcopy(base_def)
            field_def.pop("doctypes")

            if dt in doctype_overrides and fieldname in doctype_overrides[dt]:
                if doctype_overrides[dt][fieldname].get("exclude"):
                    continue
                field_def.update(doctype_overrides[dt][fieldname])

            fields[dt].append(field_def)

    new_fields = get_new_custom_fields_only(fields)
    create_custom_fields(new_fields, update=False)

def get_new_custom_fields_only(field_map: dict) -> dict:
    """Filter out existing Custom Fields to avoid overwriting modified fields."""
    result = {}
    for doctype, field_defs in field_map.items():
        for field in field_defs:
            if not frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": field["fieldname"]}):
                result.setdefault(doctype, []).append(field)
    return result

def ensure_fieldmate_flag_exists():
    """Ensure that the 'Custom Field' Doctype has a 'x_fieldmate' checkbox field."""
    if not frappe.db.exists("Custom Field", {"dt": "Custom Field", "fieldname": "x_fieldmate"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Custom Field",
            "fieldname": "x_fieldmate",
            "label": "Fieldmate Managed",
            "fieldtype": "Check",
            "insert_before": "fieldtype",
			"read_only": 1,
			"hidden": 1
        }).insert(ignore_permissions=True)
        frappe.db.commit()
        frappe.logger("fieldmate").info("Created system field: x_fieldmate on Custom Field")
