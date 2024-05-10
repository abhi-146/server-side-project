import frappe
from frappe.model.document import Document

class CustomToDo(Document):
    def validate(self):
        frappe.throw( "This class is overriden" )