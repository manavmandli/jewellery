# Copyright (c) 2024, Manav Mandli and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now


class PurchaseInvoice(Document):
    def validate(self):
        self.update_details()

    # update other details
    def on_submit(self):
        self.update_stock_balance(update=True)
        self.create_payment_ledger()
        self.create_stock_ledger()
        self.supplier_payment_tracker(update=True)

    def on_cancel(self):
        self.update_stock_balance(update=False)
        self.delete_payment_ledger()
        self.delete_stock_ledger()
        self.supplier_payment_tracker(update=False)

    def update_details(self):
        # Initialize totals to zero before calculations
        self.total_item = 0
        self.total_quantity = 0
        self.total_net_weight = 0
        self.total_amount = 0
        self.net_total = 0

        metal_rate = self.metal_rate or 0

        for item in self.items:
            item_doc = frappe.get_doc("Item", item.item)

            self.total_item += 1
            self.total_quantity += item.quantity or 0

            # Calculate pure weight
            pure_weight = ((item.weight or 0) * (item.touch or 0) / 99.99)
            self.total_net_weight += pure_weight

            # Update total amount and net total
            self.total_amount += ((item.amount or 0) * (item.quantity or 0))
            self.net_total += ((pure_weight * metal_rate) / 10) + (self.total_amount)

        # Calculate outstanding amounts
        self.outstanding_amount = self.total_amount - (self.paid_amount or 0)
        self.outstanding_metal = self.total_net_weight - (self.paid_metal or 0)

        if self.outstanding_amount == 0 and self.outstanding_metal == 0:
            self.is_paid = 1

    def update_stock_balance(self,update):
        if update:
            for itm in self.items:
                item_doc = frappe.get_doc("Item", itm.item)
                if itm.weight:
                    item_doc.item_weight = item_doc.item_weight + itm.weight
                if itm.quantity:
                    item_doc.item_quantity = item_doc.item_quantity + itm.quantity
                item_doc.save()
        else:
            for itm in self.items:
                item_doc = frappe.get_doc("Item", itm.item)
                if itm.weight:
                    item_doc.item_weight = item_doc.item_weight - itm.weight
                if itm.quantity:
                    item_doc.item_quantity = item_doc.item_quantity - itm.quantity
                item_doc.save()

    def create_payment_ledger(self):
        if self.paid_amount:
            payment_doc = frappe.get_doc(
                dict(
                    doctype="Payment Ledger",
                    date=now(),
                    supplier=self.supplier,
                    transaction_type="Debit",
                    amount=self.paid_amount,
                )
            )
            payment_doc.insert(ignore_permissions=True)
        if self.paid_metal:
            payment_doc = frappe.get_doc(
                dict(
                    doctype="Payment Ledger",
                    date=now(),
                    supplier=self.supplier,
                    transaction_type="Debit",
                    pure_metal=self.paid_metal,
                )
            )
            payment_doc.insert(ignore_permissions=True)

    def delete_payment_ledger(self):
        if self.paid_amount or self.paid_metal:
            payment_docs = frappe.get_all(
                "Payment Ledger",
                filters={
                    "supplier": self.supplier,
                    "transaction_type": "Debit",
                },
            )
            for payment_doc in payment_docs:
                frappe.delete_doc("Payment Ledger", payment_doc.name)

    def create_stock_ledger(self):
        for itm in self.items:
            stock_doc = frappe.get_doc(
				dict(
					doctype="Stock Ledger",
					item=itm.item,
					uom=itm.uom,
					weight=itm.weight or 0,
					quantity=itm.quantity or 0,
					transaction_type="Credit",
				)
			)
            stock_doc.insert(ignore_permissions=True)

    def delete_stock_ledger(self):
        for itm in self.items:
            stock_docs = frappe.get_all(
                "Stock Ledger",
                filters={
                    "item": itm.item,
                    "transaction_type": "Credit",
                },
            )
            for stock_doc in stock_docs:
                frappe.delete_doc("Stock Ledger", stock_doc.name)

    def supplier_payment_tracker(self, update):
        if not frappe.db.exists("Supplier Payment Tracker", self.supplier):
            payment_tracker_doc = frappe.get_doc(
                dict(
                    doctype="Supplier Payment Tracker",
                    supplier=self.supplier,
                    pending_amount=self.outstanding_amount,
                    pending_metal=self.outstanding_metal,
                    created_on=now(),
                )
            )
            payment_tracker_doc.insert(ignore_permissions=True)
            frappe.db.commit()
        else:
            if update:
                payment_tracker_doc = frappe.get_doc(
                    "Supplier Payment Tracker", self.supplier
                )
                payment_tracker_doc.pending_amount += self.outstanding_amount
                payment_tracker_doc.pending_metal += self.outstanding_metal
                payment_tracker_doc.updated_on = now()
                payment_tracker_doc.save(ignore_permissions=True)
                frappe.db.commit()
            else:
                payment_tracker_doc = frappe.get_doc(
                    "Supplier Payment Tracker", self.supplier
                )
                payment_tracker_doc.pending_amount -= self.outstanding_amount
                payment_tracker_doc.pending_metal -= self.outstanding_metal
                payment_tracker_doc.updated_on = now()
                payment_tracker_doc.save(ignore_permissions=True)
                frappe.db.commit()
