frappe.ui.form.on("Item Details", {
  uom(frm) {
    if (frm.doc.uom == "Piece") {
      frm.set_df_property("touch", "hidden", 1);
      frm.set_df_property("weight", "hidden", 1);
      frm.set_df_property("quantity", "reqd", 1);
      frm.set_df_property("amount", "reqd", 1);
    }
  },
});
