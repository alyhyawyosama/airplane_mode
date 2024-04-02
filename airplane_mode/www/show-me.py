import frappe



def get_context(context):
	# get color from the color paramerter in the url 
    
    page_color =  frappe.form_dict.get("color") if frappe.form_dict.get("color") else "black" 
    context.page_color = page_color
    context.statement = "OSAma alyhaywy"
    return context