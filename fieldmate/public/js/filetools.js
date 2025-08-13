// fieldmate/public/js/filetools.js
(function () {
  const WEBSITE_FOLDER = "Home/Website";

  function inWebsiteFolder(folder) {
    // exact match OR any nested path like WEBSITE_FOLDER
    return folder === WEBSITE_FOLDER || (folder && folder.startsWith(WEBSITE_FOLDER + "/"));
  }

  function isWebsiteContext(frm) {
    const d = frm.doc || {};
    // Only public files in website folder
    return !d.is_private && inWebsiteFolder(d.folder || "");
  }

  function maybeAutoCheck(frm) {
    if (!frm.is_new()) return;
    if (!isWebsiteContext(frm)) return;

    const current = frm.doc.x_fileReplace;
    const userOverrode = frm._user_overrode_replace === true;

    if ((current === 0 || current == null || frm._auto_suggested_replace) && !userOverrode) {
      frm._auto_suggested_replace = true;
      frm.set_value("x_fileReplace", 1);
    }
  }

  frappe.ui.form.on("File", {
    refresh(frm) {
      maybeAutoCheck(frm);
      // Respect manual change
      if (frm.fields_dict.x_fileReplace && frm.fields_dict.x_fileReplace.$input) {
        frm.fields_dict.x_fileReplace.$input.on("change", () => {
          frm._user_overrode_replace = true;
        });
      }
    },
    // Re-evaluate if user changes folder or privacy before saving
    folder(frm) {
      maybeAutoCheck(frm);
    },
    is_private(frm) {
      maybeAutoCheck(frm);
    },
    validate(frm) {
      maybeAutoCheck(frm);
    },
  });
})();
