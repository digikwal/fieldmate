import frappe
import os
import json

EXCLUDED_KEYS = ["name", "creation", "modified", "owner", "modified_by", "idx"]

def export_fieldmate_fields(verbose=False):
    """Export all x_fieldmate=1 fields to JSON, and clean up deleted ones."""
    export_path = frappe.get_app_path("fieldmate", "custom_field")
    os.makedirs(export_path, exist_ok=True)

    # Track exported filenames
    exported_files = set()

    # Fetch current active custom fields
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
        exported_files.add(filename)

        # Skip if file already matches
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if existing == data:
                continue

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=True, default=str)

        log(f"Exported: {filename}", verbose)

    # Clean up obsolete files
    all_files = {f for f in os.listdir(export_path) if f.endswith(".json")}
    obsolete = all_files - exported_files
    for filename in obsolete:
        os.remove(os.path.join(export_path, filename))
        log(f"Deleted: {filename}", verbose)
        # Optional: stage for git
        os.system(f"git rm --quiet --cached '{os.path.join(export_path, filename)}' || true")

def sanitize_field_data(data: dict) -> dict:
    """Strip system metadata from field JSON."""
    return {k: v for k, v in data.items() if k not in EXCLUDED_KEYS}

def log(message: str, verbose: bool = False):
    if verbose:
        print(message)
    else:
        frappe.logger("fieldmate").info(message)
