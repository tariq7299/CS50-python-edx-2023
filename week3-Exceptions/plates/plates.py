def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    plate_digits = []

    if len(s) > 6 or len(s) < 2:
        return False
    for index, char in enumerate(s):
        if not char.isalnum():
            return False
        if char.isdigit() and index != len(s)-1:
            plate_digits.append(char)
            if s[index+1].isalpha():
                return False
            if plate_digits[0] == "0":
                return False

    return True
main()

