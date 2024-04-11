from validator_collection import validators, checkers, errors

email = input("Enter email: ")

if checkers.is_email(email):
    print("Valid")
else:
    print("Invalid")
