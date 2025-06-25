def test_field_templates_exist():
    from fieldmate.setup import custom_fields
    assert hasattr(custom_fields, "setup_custom_fields")
