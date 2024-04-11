def main():
    # Takes input from user
    plate = input("Plate: ")
    # If is_valid() function returns True, print valid
    if is_valid(plate):
        print("Valid")
    # If is_valid() returns False, print Invalid
    else:
        print("Invalid")


def is_valid(s):
    # An empty list which will contain later all the digits found in the input of user
    plate_digits = []

    # If the Characters count in "s" (the user input), is less then 2 chars it will be false, or if the Characters count is more than 6 then also it will be false
    if len(s) > 6 or len(s) < 2:
        return False
    for index, char in enumerate(s):
        # If the character is not a letter or a digit then False
        if not char.isalnum():
            return False
        # Here We will check if the digits in the string (plate text), is followed by a letter or not
        # Also we will check whether the first digit in the text is "zero" or not
        # I wrote "index != len(s)-1" to make sure I do not try access an element with an index outside "s" boundries while using s[index+1]
        if char.isdigit() and index != len(s)-1:
            plate_digits.append(char)
        # If the character is a number, then here we will make sure it is not followed by a letter (on of the rules of the vanity plates)
        # And I achieved this by keep asking in every iteration if the digit is followed by a letter.
            if s[index+1].isalpha():
                return False
            if plate_digits[0] == "0":
                return False

    return True
main()

