from validate_email import validate_email
email = input("Enter your email_id: ")
is_valid = validate_email(email)
print(is_valid)