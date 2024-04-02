# Copyright (c) 2024, OSAma and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	# before save set to full name field the first name and last name 
 	def before_save(self):
 		self.full_name = self.first_name + " " + self.last_name
