import frappe
import os
import json

EXCLUDED_KEYS = ["name", "creation", "modified", "owner", "modified_by", "idx"]

def export_fieldmate_fields(verbose=False):
    """Export all Custom Fields with x_fieldmate = 1 to individual JSON files."""
    export_path = frappe.get_app_path("fieldmate", "custom_field")
    os.makedirs(export_path, exist_ok=True)

    custom_fields = frappe.get_all(
        "Custom Field",
        filters={"x_fieldmate": 1},
        fields=["name", "dt", "fieldname"]
    )

    for field in custom_fields:
        doc = frappe.get_doc("Custom Field", field["name"])
        data = sanitize_field_data(doc.as_dict())

        filename = f'{field["dt"]}--{field["fieldname"]}.json'.replace(" ", "_")
        file_path = os.path.join(export_path, filename)

        # Avoid unnecessary overwrite if file exists and hasn't changed
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if existing == data:
                continue  # No changes

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=True, default=str)

        log_message = f"Exported: {filename}"
        if verbose:
            print(f"{log_message}")
        else:
            frappe.logger("fieldmate").info(log_message)

def sanitize_field_data(data: dict) -> dict:
    """Prepare field dict for export by removing runtime/system values."""
    return {k: v for k, v in data.items() if k not in EXCLUDED_KEYS}
