// Copyright (c) 2024, Manav Mandli and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sales Invoice", {
  city(frm) {
    frm.set_query("customer", function () {
      return {
        filters: {
          city: frm.doc.city,
        },
      };
    });
  },
});
