import pytest

@pytest.mark.integration
def test_setup_custom_fields_runs():
    from fieldmate.setup import setup_custom_fields
    setup_custom_fields()
