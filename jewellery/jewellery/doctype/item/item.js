// Copyright (c) 2024, Manav Mandli and contributors
// For license information, please see license.txt

frappe.ui.form.on("Item", {
  unit_of_measure(frm) {
    if (frm.doc.unit_of_measure === "Piece") {
      set_read_only_fields(frm, false, true); // Quantity editable, Weight read-only
    } else if (frm.doc.unit_of_measure === "Gram") {
      set_read_only_fields(frm, true, false); // Quantity read-only, Weight editable
    } else {
      set_read_only_fields(frm, false, false); // Both editable
    }
  },
});

// Helper function to set read-only status
function set_read_only_fields(frm, quantity_read_only, weight_read_only) {
  frm.set_df_property("item_quantity", "read_only", quantity_read_only ? 1 : 0);
  frm.set_df_property("item_weight", "read_only", weight_read_only ? 1 : 0);
}
