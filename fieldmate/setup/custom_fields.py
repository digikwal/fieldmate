import frappe
from copy import deepcopy
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

"""
Custom Field Setup Utility

- All custom fields managed by Fieldmate should start with 'x_'.
- Field definitions are provided as dicts in `field_templates`.
- Doctypes field specifies one or more doctypes to which fields should be added.
- If a field requires doctype-specific configuration, use `doctype_overrides`.
- This function ensures the 'x_fieldmate' flag exists, prepares field definitions,
  applies overrides, and creates only new custom fields (does not overwrite existing ones).
"""
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
        },
        "x_href": {
            "fieldname": "x_href",
            "label": "Custom html reference",
            "fieldtype": "Data",
            "insert_after": "file_size",
            "x_fieldmate": 1,
            "doctypes": ["File"]
        }
    }

    # Per-doctype overrides for field placement or exclusion
    doctype_overrides = {
        "Company": {
            "x_coc": {
                "insert_after": "default_holiday_list"
            }
        }
    }

    # Collect all target doctypes from field templates
    target_doctypes = list({dt for f in field_templates.values() for dt in f["doctypes"]})
    fields = {dt: [] for dt in target_doctypes}

    # Build field definitions for each doctype, applying overrides if present
    for fieldname, base_def in field_templates.items():
        for dt in base_def.get("doctypes", []):
            field_def = deepcopy(base_def)
            field_def.pop("doctypes") # Remove doctypes key for actual field definition

            # Apply doctype-specific overrides if available
            if dt in doctype_overrides and fieldname in doctype_overrides[dt]:
                # Skip field if explicitly excluded
                if doctype_overrides[dt][fieldname].get("exclude"):
                    continue
                field_def.update(doctype_overrides[dt][fieldname])

            fields[dt].append(field_def)

    # Filter out fields that already exist to avoid overwriting user changes
    new_fields = get_new_custom_fields_only(fields)
    # Create only the new custom fields (no update of existing fields)
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
			"hidden": 1,
			"in_list_view": 0,
			"no_copy": 1,
			"print_hide": 1
        }).insert(ignore_permissions=True)
        frappe.db.commit()
        frappe.logger("fieldmate").info("Created system field: x_fieldmate on Custom Field")
