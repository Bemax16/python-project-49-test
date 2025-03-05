import math
import random


def play_gcd_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        answer = input("Your answer: ").strip()

        correct_answer = math.gcd(num1, num2)

        if answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    play_gcd_game()


if __name__ == "__main__":
    play_gcd_game()
