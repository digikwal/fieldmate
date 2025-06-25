import os
import json
import frappe
import pytest

@pytest.mark.export
def test_all_custom_field_json_valid():
    path = frappe.get_app_path("fieldmate", "custom_fields")
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            with open(os.path.join(path, filename), "r") as f:
                try:
                    data = json.load(f)
                    assert "fieldname" in data
                except Exception as e:
                    assert False, f"Invalid JSON in {filename}: {e}"
