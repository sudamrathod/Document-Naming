import frappe

def  validate(doc, method):
    if doc.is_new():
        item_name = doc.item_name.replace(" ", "_") if doc.item_name else "Item"
        reservation = doc.custom_revision
        operation = doc.custom_operation
        if reservation and operation:
            # Construct custom name
            doc.name = f"{item_name}_{reservation}_{operation}"