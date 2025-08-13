app_name = "fieldmate"
app_title = "Fieldmate"
app_publisher = "Digikwal"
app_description = "Custom field extension and quality of life improvements"
app_email = "help@digikwal"
app_license = "MIT"

# Run on app install or migrate
before_app_install = "fieldmate.setup.install.before_app_install"
after_app_install = "fieldmate.setup.install.after_app_install"
after_migrate = [
    "fieldmate.setup.custom_fields.setup_custom_fields",
    "fieldmate.setup.install.ensure_website_folder",
]

# Trigger on DOC events
doc_events = {
    "Custom Field": {
        "on_update": "fieldmate.setup.export_fieldmate_fields",
        "on_trash": "fieldmate.setup.export_fieldmate_fields",
    },
    "File": {
        "after_insert": "fieldmate.filetools.replace.on_file_after_insert",
    },
}

# Client-side JS
doctype_js = {
    "File": "public/js/filetools.js",
}