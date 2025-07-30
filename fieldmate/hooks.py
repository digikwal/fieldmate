app_name = "fieldmate"
app_title = "Fieldmate"
app_publisher = "Digikwal"
app_description = "Custom field extension and web frontend"
app_email = "help@digikwal"
app_license = "mit"

# Run on app install or migrate
before_app_install = "fieldmate.setup.install.before_app_install"
after_app_install = "fieldmate.setup.install.after_app_install"
after_migrate = "fieldmate.setup.custom_fields.setup_custom_fields"

# Export x_fieldmate fields on update
doc_events = {
    "Custom Field": {
        "on_update": "fieldmate.setup.export_fieldmate_fields",
		"on_trash": "fieldmate.setup.export_fieldmate_fields"
    }
}

# Include custom CSS and JS files for website
web_include_css = "/assets/fieldmate/css/main.css"