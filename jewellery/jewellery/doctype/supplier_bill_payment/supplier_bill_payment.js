// Copyright (c) 2024, Manav Mandli and contributors
// For license information, please see license.txt

frappe.ui.form.on("Supplier Bill Payment", {
    supplier(frm){
        get_outstanding_payment_detaills(frm);
    }
});

function get_outstanding_payment_detaills(frm){
    frappe.call({
        method: "jewellery.jewellery.doctype.supplier_bill_payment.supplier_bill_payment.get_outstanding_payment_details",
        args: {
            supplier: frm.doc.supplier
        },
        callback: function (r) {
            if (r.message) {
                frm.set_value("outstanding_amount", r.message.pending_amount);
                frm.set_value("outstanding_metal", r.message.pending_metal);
            } else {
                frm.set_value("outstanding_amount", 0);
                frm.set_value("outstanding_metal", 0);
            }
            frm.refresh();
        }
    });
}
