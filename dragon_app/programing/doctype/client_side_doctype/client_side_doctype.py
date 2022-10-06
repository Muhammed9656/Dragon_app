# Copyright (c) 2022, MUHAMMED and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class ClientSidedoctype(Document):
	pass

@frappe.whitelist()
def frappe_call(msg):
    import time
    time.sleep(5)
    frappe.msgprint(msg)
    
    # return "Hi This message from frappe_call"
    
        
 