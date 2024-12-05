
def valid_phone(phone):
    if not phone.isdigit():
        return False, "Phone must be numeric integer degit."
    return True, ""

def valid_name(name):
    if not name.isalpha():
        return False, "Name must be alphanumeric."
    return True, ""

def valid_email(email):
    if '@' not in email:
        return False, "Invalid email! The email format must contain '@'."
    return True, ""
