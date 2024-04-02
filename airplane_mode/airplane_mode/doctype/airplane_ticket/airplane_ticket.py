# Copyright (c) 2024, OSAma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random



class AirplaneTicket(Document):
	def validate(self):
		used_items = [] #To check the exist item 
		new_items = [] # To save in the table only the distinct items 
		for item in self.add_ons  :
			# To check the unique items
			if item.item not in used_items : 
				used_items.append(item.item)
				new_items.append(item)
			else :
				frappe.msgprint((f"The <b>{item.item}</b> item is already exist"))

		self.add_ons = new_items
		self.clculate_total_amount()
  
  
	def clculate_total_amount(self):
		'''To calculate the total price of fight and add_ons items'''
		total_amount = self.flight_price 
		for item in self.add_ons  :
			#To calculate the total amount of items  
			total_amount += item.amount
		self.total_amount = total_amount 

	
	def before_insert(self):
     	#To set value to the seat field before insert the document to the db 
     
		# Randome value has an expression =>  <random-integer><random-capital-alphabet-from-A-to-E>
		alphbet_range = ['A','B','C','D','E']
		exp = str(random.randint(1,99))+str(random.choice(alphbet_range)) 
		self.seat = exp 

	
	
        




		

