import frappe

# White listed 
@frappe.whitelist()
def custom_number_card():
    return {
	"value": 100,
	"fieldtype": "Currency",
	"route_options": {"from_date": "2023-05-23"},
}

@frappe.whitelist()
def sales_order_number_card():
    count = frappe.db.sql("""SELECT COUNT(*) FROM `tabSales Order`""")
    return {
	"value": count,
	"fieldtype": "Float",
	"route_options": {"from_date": "2023-05-23"},
}