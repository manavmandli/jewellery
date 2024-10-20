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
  item: function (frm, cdt, cdn) {
    const row = locals[cdt][cdn];
    if (row.uom == "Piece") {
      frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].toggle_editable('touch', false);
      frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].toggle_editable('weight', false);
      frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].toggle_editable('quantity', true);
      frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].toggle_editable('amount', true);
    }
    else if (row.uom == "Metal") {
      frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].toggle_editable('touch', true);
      frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].toggle_editable('weight', true);
      frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].toggle_editable('quantity', false);
      frm.fields_dict['items'].grid.grid_rows_by_docname[cdn].toggle_editable('amount', false);
    }
    frm.refresh_field("items"); 
  },
});
