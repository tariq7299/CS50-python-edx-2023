import random

def main():

    level = get_level()

    score = 0

    for _ in range(10):
        attempts = 0
        num1 = generate_integer(level)
        num2 = generate_integer(level)

        while attempts < 3:

            try:
                correct_answer = num1 + num2
                answer = int(input(f"{num1} + {num2} = "))

                if answer == correct_answer:
                    score += 1
                    break
                else:
                    raise Exception

            except Exception:
                print("EEE")
                attempts += 1
                if attempts == 3:
                    print(f"The correct answer is {correct_answer}")

    print(f"Score: {score}")

def get_level():
    while True:

        try:
            level = int(input("Enter level (1, 2, or 3): "))
            if 1 <= level <= 3:
                break
        except Exception:
            pass

    return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
if __name__ == "__main__":
    main()
