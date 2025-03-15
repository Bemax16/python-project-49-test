import math
import random

from brain_games.scripts import interface


def play_gcd_game():
    name = interface.start_game()

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        answer = input("Your answer: ").strip()

        correct_answer = math.gcd(num1, num2)

        correct_answers += interface.check_answer(answer, correct_answer)

    print(f"Congratulations, {name}!")


def main():
    play_gcd_game()


if __name__ == "__main__":
    play_gcd_game()
