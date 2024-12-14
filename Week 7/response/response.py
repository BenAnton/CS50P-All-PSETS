from validator_collection import validators, errors

def main():
    email_address = input("Email: ")
    try:
        validators.email(email_address, allow_empty = False)
        print("Valid")
    except errors.InvalidEmailError:
        print("Invalid")

main()
