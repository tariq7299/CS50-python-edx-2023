
def main():

    while True:
        text = input("text: ").strip()
        if text:
            break
    new_word = shorten(text)
    print(new_word)


def shorten(word):
    new_word = ""
    for letter in word:
        if letter.lower() not in ["a", "e" , "i", "o", "u"]:
            new_word += letter
    return new_word

if __name__ == "__main__":
    main()
