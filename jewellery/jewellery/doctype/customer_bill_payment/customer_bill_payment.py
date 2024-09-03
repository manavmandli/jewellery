# Copyright (c) 2024, Manav Mandli and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class CustomerBillPayment(Document):
    def on_submit(self):
        self.update_customer_payment_tracker()
        self.create_payment_ledger()

    def update_customer_payment_tracker(self):
        if frappe.db.exists("Customer Payment Tracker", self.customer):
            customer_payment_doc = frappe.get_doc(
                "Customer Payment Tracker", self.customer
            )
            customer_payment_doc.pending_amount -= self.amount
            customer_payment_doc.pending_metal -= self.weight
            customer_payment_doc.updated_on = datetime.now()
            customer_payment_doc.save()
        else:
            new_customer_payment_tracker = frappe.get_doc(
                {
                    "doctype": "Customer Payment Tracker",
                    "customer": self.customer,
                    "pending_amount": -self.amount,
                    "pending_metal": -self.weight,
                    "created_on": datetime.now(),
                    "updated_on": datetime.now(),
                }
            )
            new_customer_payment_tracker.insert()

    def create_payment_ledger(self):
        payment_ledger_doc = frappe.get_doc(
            {
                "doctype": "Payment Ledger",
                "customer": self.customer,
                "transaction_type": "Credit",
                "pure_metal": self.weight,
                "amount": self.amount,
                "date": datetime.now(),
            }
        )
        payment_ledger_doc.insert()
