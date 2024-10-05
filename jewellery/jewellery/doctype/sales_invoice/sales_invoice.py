# Copyright (c) 2024, Manav Mandli and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SalesInvoice(Document):
    def validate(self):
        # form intenal calculation
        self.update_details()

    # update other details
    def on_submit(self):
        self.update_stock_balance(self)
        self.create_payment_ledger(self)
        self.create_stock_ledger(self)
        self.customer_payment_tracker(self)

    def update_details(self):
        # Initialize totals to zero before calculations
        self.total_item = 0
        self.total_quantity = 0
        self.total_net_weight = 0
        self.total_amount = 0
        self.net_total = 0

        metal_rate = self.metal_rate or 0

        for item in self.items:
            self.total_item += 1
            self.total_quantity += item.quantity or 0

            # Calculate pure weight
            pure_weight = (item.weight * item.touch) / 99.99
            self.total_net_weight += pure_weight

            # Update total amount and net total
            self.total_amount += item.amount or 0
            self.net_total += pure_weight * metal_rate

        # Calculate outstanding amounts
        self.outstanding_amount = self.total_amount - (self.paid_amount or 0)
        self.outstanding_metal = self.total_net_weight - (self.paid_metal or 0)

    def update_stock_balance(self):
        pass

    def create_payment_ledger(self):
        pass

    def create_stock_ledger(self):
        pass

    def customer_payment_tracker(self):
        pass
