import inflect

                    # First solution
def main():

    p = inflect.engine()

    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    joined_names = p.join(names)
    print("Adieu, adieu, to " + joined_names)


main()



                    # Second solution
# def main():

#     names = []

#     while True:
#         try:
#             name = input("Name: ")
#             names.append(name)
#         except EOFError:
#             print()
#             break

#     # print(names)
#     joined_names = join_words(names)
#     print(joined_names)

# def join_words(words):
#     # If the list is empty, return an empty string
#     if not words:
#         return ""

#     # If the list only contains one word, return that word
#     if len(words) == 1:
#         return "Adieu, adieu, to " + words[0]

#     # Join all words except the last one with commas, and add the last word with "and" before it
#     return "Adieu, adieu, to " + ", ".join(words[:-1]) + " and " + words[-1]


# main()
