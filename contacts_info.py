
contacts_info = {}

def add_contact(name, email, phone, address):
    if phone in contacts_info:
        return f"Error: The phone number {phone} already exists."
    contacts_info[phone] = {"name": name, "email": email, "address": address}
    return f"Contact for {name} added successfully."

def view_contacts():
    if not contacts_info:
        return "No contacts are available!."
    output = "Name\t\tEmail\t\tPhone\t\tAddress\n"
    output += "-" * 60 + "\n"
    for phone, details in contacts_info.items():
        output += f"{details['name']}\t{details['email']}\t{phone}\t{details['address']}\n"
    return output

def remove_contact(phone):
    if phone in contacts_info:
        del contacts_info[phone]
        return f"Contact with phone number {phone} removed."
    return f"Error: Contact with phone number {phone} not found."
