while True:
    text = input("text: ").strip()
    if text:
        break


for letter in text:
    if letter.lower() not in ["a", "e" , "i", "o", "u"]:
        print(letter, end="")
print()
