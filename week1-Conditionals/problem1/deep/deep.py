



# This propmts the user for input
user_input = input("What is the Answer to the Great Question of life, the Universe and Everything ? ")

# this will convert the user answer to all lower cases, in order to make the checking process case insesitive
# Alos it will remove any i¥unnecessary spaces by using strip()
user_input = user_input.lower().strip()


# This nice looking if statament will compare the user answer to any of the potentional correct answers
if user_input == "42" or user_input == "forty two" or user_input == "forty-two":
    print("Yes")
else :
    print("No")



# List of correct answers
# CorrectAnswers = ["42", "forty two", "forty-two"]

# This is another way to do it using a loop and a list
# if user_input in CorrectAnswers:
#     print("Yes")
# else :
#     print("No")
