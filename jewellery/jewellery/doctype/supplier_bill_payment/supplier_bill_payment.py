# Copyright (c) 2024, Manav Mandli and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class SupplierBillPayment(Document):
    def on_submit(self):
        self.update_supplier_payment_tracker(update=True)
        self.create_payment_ledger()

    def on_cancel(self):
        self.update_supplier_payment_tracker(update=False)
        self.delete_payment_ledger()

    def update_supplier_payment_tracker(self,update):
        if not frappe.db.exists("Supplier Payment Tracker", self.supplier):
            new_supplier_payment_tracker = frappe.get_doc(
                {
                    "doctype": "Supplier Payment Tracker",
                    "supplier": self.supplier,
                    "pending_amount": -self.amount,
                    "pending_metal": -self.metal,
                    "created_on": datetime.now(),
                    "updated_on": datetime.now(),
                }
            )
            new_supplier_payment_tracker.insert()
        else:
            if update:
                supplier_payment_doc = frappe.get_doc(
                    "Supplier Payment Tracker", self.supplier
                )
                supplier_payment_doc.pending_amount -= self.amount
                supplier_payment_doc.pending_metal -= self.metal
                supplier_payment_doc.updated_on = datetime.now()
                supplier_payment_doc.save()
                frappe.db.commit()
            else:
                supplier_payment_doc = frappe.get_doc(
                    "Supplier Payment Tracker", self.supplier
                )
                supplier_payment_doc.pending_amount += self.amount
                supplier_payment_doc.pending_metal += self.metal
                supplier_payment_doc.updated_on = datetime.now()
                supplier_payment_doc.save()
                frappe.db.commit()

    def create_payment_ledger(self):
        if self.amount:
            payment_doc = frappe.get_doc(
                dict(
                    doctype="Payment Ledger",
                    date=datetime.now(),
                    supplier=self.supplier,
                    transaction_type="Debit",
                    amount=self.amount,
                    reference_doctype=self.name,
                    reference_doctype_name=self.doctype,
                )
            )
            payment_doc.insert(ignore_permissions=True)
        if self.metal:
            payment_doc = frappe.get_doc(
                dict(
                    doctype="Payment Ledger",
                    date=datetime.now(),
                    supplier=self.supplier,
                    transaction_type="Debit",
                    pure_metal=self.metal,
                    reference_doctype=self.name,
                    reference_doctype_name=self.doctype,
                )
            )
            payment_doc.insert(ignore_permissions=True)

    def delete_payment_ledger(self):
        if self.amount or self.metal:
            payment_docs = frappe.get_all(
                "Payment Ledger",
                filters={
                    "reference_doctype": self.name,
                    "reference_doctype_name": self.doctype,
                },
            )
            for payment_doc in payment_docs:
                frappe.delete_doc("Payment Ledger", payment_doc.name)


@frappe.whitelist()
def get_outstanding_payment_details(supplier):
    if not supplier:
        return {"pending_amount": 0, "pending_metal": 0}

    get_outstandings = frappe.db.get_value(
        "Supplier Payment Tracker",
        {"supplier": supplier},
        ["pending_amount", "pending_metal"],
        as_dict=True,
    )

    if not get_outstandings:
        return {"pending_amount": 0, "pending_metal": 0}

    return get_outstandings
