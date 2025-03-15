import random

from brain_games.engine import run_game


def generate_progression():
    length = random.randint(5, 10)
    difference = random.randint(1, 5)
    start = random.randint(1, 10)

    progression = [start + i * difference for i in range(length)]
    missing_index = random.randint(0, length - 1)

    correct_answer = progression[missing_index]
    progression[missing_index] = ".."

    return " ".join(map(str, progression)), correct_answer


def main():
    run_game(generate_progression, "What number is missing in the progression?")


if __name__ == "__main__":
    main()
