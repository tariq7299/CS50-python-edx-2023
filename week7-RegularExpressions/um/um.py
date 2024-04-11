import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Here I have used re.findall()
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)

    # This will calculate the number of ums in matches
    return len(matches)

if __name__ == "__main__":
    main()
