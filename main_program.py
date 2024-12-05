
from contacts_info import add_contact, view_contacts, remove_contact
from save_file import contacts_save, contacts_load
from validation_check import valid_name, valid_phone, valid_email


def menu():
    print("\nContact Information")
    print("1. Add Contact Information")
    print("2. View Contacts Information")
    print("3. Remove Contact")
    print("4. Exit")


def main():
    print("Welcome to the Contact Diary!")
    contacts_load()

    while True:
        menu()
        choice = input("Select an option : ")

        if choice == '1':
            name = input("Enter name: ")
            is_valid_name, name_msg = valid_name(name)
            if not is_valid_name:
                print(name_msg)
                continue

            email = input("Enter email: ")
            is_valid_email, email_msg = valid_email(email)
            if not is_valid_email:
                print(email_msg)
                continue

            phone = input("Enter phone number: ")
            is_valid_phone, phone_msg = valid_phone(phone)
            if not is_valid_phone:
                print(phone_msg)
                continue

            address = input("Enter address: ")
            result = add_contact(name, email, phone, address)
            print(result)

        elif choice == '2':
            print(view_contacts())

        elif choice == '3':
            phone = input("Enter phone number of the contact to remove: ")
            result = remove_contact(phone)
            print(result)

        elif choice == '4':
            print(contacts_save())
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
