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

frappe.ui.form.on("Item Details", {
  uom(frm, cdt, cdn) {
    const row = locals[cdt][cdn];
    if (row.uom == "Piece") {
      frappe.meta.get_docfield(
        "Item Details",
        "touch",
        frm.doc.name
      ).hidden = 1;
      frappe.meta.get_docfield(
        "Item Details",
        "weight",
        frm.doc.name
      ).hidden = 1;
      frappe.meta.get_docfield(
        "Item Details",
        "quantity",
        frm.doc.name
      ).reqd = 1;
      frappe.meta.get_docfield("Item Details", "amount", frm.doc.name).reqd = 1;
    } else {
      frappe.meta.get_docfield(
        "Item Details",
        "touch",
        frm.doc.name
      ).hidden = 0;
      frappe.meta.get_docfield(
        "Item Details",
        "weight",
        frm.doc.name
      ).hidden = 0;
      frappe.meta.get_docfield(
        "Item Details",
        "quantity",
        frm.doc.name
      ).reqd = 0;
      frappe.meta.get_docfield("Item Details", "amount", frm.doc.name).reqd = 0;
    }
    frm.refresh_field("item_details"); // Ensure the child table refreshes
  },
});
