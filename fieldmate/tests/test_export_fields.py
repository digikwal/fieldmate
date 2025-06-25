import pytest

@pytest.mark.export
def test_export_does_not_crash():
    from fieldmate.setup import export_fieldmate_fields
    export_fieldmate_fields()
