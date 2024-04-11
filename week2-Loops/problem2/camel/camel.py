

def main():
                       # The FIRST method #

    # This will keep prompting the user for an str
    while True:
        text = input("camelCase: ").strip()
        if text:
            break
    # An index temp, that I will use inside my for loop
    indexTemp = 0
    #Empty var, that will contain a snake cased word
    snake_word = ''
    # Empty var, that will contain the all snake cased words
    snake_text = ''

    for letterIndex, letter in enumerate(text):
        if letter.isupper():
            upperLetterIndex = letterIndex
            word = text[indexTemp:upperLetterIndex]
            snake_word = word + "_"
            snake_text = snake_text + snake_word
            indexTemp = upperLetterIndex
    restOfText = text[indexTemp:]
    snake_text = snake_text + restOfText

    snake_text = snake_text.lower()
    print(snake_text)

                    # The SECOND method which uses "re" module #
# import re
#     while True:
#         text = input("camelCase: ").strip()
#         if text:
#             break
#     snake_text = camel_to_snake(text)
#     print(snake_text)


# def camel_to_snake(camel_case_string):
#     return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()



                    # The THIRD method, the simplest method

    # while True:
    #     text = input("camelCase: ").strip()
    #     if text:
    #         break


    # for letter in text:
    #     if letter.isupper():
    #         print("_" + letter.lower(), end="")
    #     else:
    #         print(letter, end="")
    # print()

main()