# Copyright (c) 2024, OSAma and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
# from frappe.model.document import Document



class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		# Set the Status field to Completed after the document is submitted.
		self.status = "Completed" 
		#get list of tiket that have the same flight name 
		tikets = frappe.get_all("Airplane Ticket", filters={"flight": self.name})
		for tiket in tikets:
			#Get the ticket 
			tiket_doc = frappe.get_doc("Airplane Ticket", tiket.name)
			# method to submit all Airplane Tickets that are linked to an Airplane Flight and are Boarded on the submission of an Airplane Flight document
			if tiket_doc and tiket_doc.docstatus == 0 and tiket_doc.status == "Boarded":
				tiket_doc.submit()
				tiket_doc.save()
		#save the document







