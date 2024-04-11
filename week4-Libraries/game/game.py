import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level > 0 :
            break
    except Exception:
        pass


target = random.randint(1, level)


while True:

    while True:
        try:
            user_guess = int(input("Guess: "))
            break
        except Exception:
            pass

    if user_guess == target:
        print("Just right!")
        break

    elif user_guess > target:
        print("Too large!")

    elif user_guess < target:
        print("Too small!")

