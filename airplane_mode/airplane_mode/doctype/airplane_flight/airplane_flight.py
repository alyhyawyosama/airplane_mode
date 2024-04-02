# Copyright (c) 2024, OSAma and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
# from frappe.model.document import Document



class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		# Set the Status field to Completed after the document is submitted.
		self.status = "Completed" 





