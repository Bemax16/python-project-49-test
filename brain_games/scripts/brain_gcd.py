import random
import math
from brain_games.engine import run_game


def game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)

    return question, correct_answer


def main():
    run_game(game_logic, "Find the greatest common divisor of given numbers.")


if __name__ == "__main__":
    main()
