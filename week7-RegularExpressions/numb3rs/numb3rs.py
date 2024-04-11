import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # First solution
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        if 0 <= int(matches.group(1)) <= 255 and 0 <= int(matches.group(2)) <= 255 and 0 <= int(matches.group(3)) <= 255 and 0 <= int(matches.group(4)) <= 255:
            return True
        else:
            return False
    else:
        return False

    # Second solution
    # if match := re.match(r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)", ip):
    #     return "valid"
    # else:
    #     return "invalid"

if __name__ == "__main__":
    main()
