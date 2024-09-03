# Copyright (c) 2024, Manav Mandli and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class SupplierBillPayment(Document):
    def on_submit(self):
        self.update_supplier_payment_tracker()
        self.create_payment_ledger()

    def update_supplier_payment_tracker(self):
        if frappe.db.exists("Supplier Payment Tracker", self.supplier):
            supplier_payment_doc = frappe.get_doc(
                "Supplier Payment Tracker", self.supplier
            )
            supplier_payment_doc.pending_amount -= self.amount
            supplier_payment_doc.pending_metal -= self.weight
            supplier_payment_doc.updated_on = datetime.now()
            supplier_payment_doc.save()
        else:
            new_supplier_payment_tracker = frappe.get_doc(
                {
                    "doctype": "Supplier Payment Tracker",
                    "supplier": self.supplier,
                    "pending_amount": -self.amount,
                    "pending_metal": -self.weight,
                    "created_on": datetime.now(),
                    "updated_on": datetime.now(),
                }
            )
            new_supplier_payment_tracker.insert()

    def create_payment_ledger(self):
        payment_ledger_doc = frappe.get_doc(
            {
                "doctype": "Payment Ledger",
                "customer": self.supplier,
                "transaction_type": "Credit",
                "pure_metal": self.weight,
                "amount": self.amount,
                "date": datetime.now(),
            }
        )
        payment_ledger_doc.insert()
