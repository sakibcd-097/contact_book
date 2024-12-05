
import csv
from contacts_info import contacts_info

def contacts_save(filename="contacts.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Email", "Phone", "Address"])
            for phone, details in contacts_info.items():
                writer.writerow([details["name"], details["email"], phone, details["address"]])
        return "Contacts are saved successfully."
    except Exception as e:
        return f"Warning saving contacts: {str(e)}"

def contacts_load(filename="contacts.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name, email, phone, address = row
                contacts_info[phone] = {"name": name, "email": email, "address": address}
        return "Contacts are loaded successfully."
    except FileNotFoundError:
        return "No saved contacts are found. Start Again."
    except Exception as e:
        return f"Warning loading contacts: {str(e)}"
