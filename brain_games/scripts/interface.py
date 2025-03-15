import sys


def start_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    return name


def check_answer(answer, correct_answer, name):
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
        )
        print(f"Let's try again, {name}!")
        sys.exit()

