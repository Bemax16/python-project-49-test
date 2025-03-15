import random

from brain_games.engine import run_game


def game_logic():
    number = random.randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"

    return number, correct_answer


def main():
    run_game(game_logic, 'Answer "yes" if the number is even, '
                         'otherwise answer "no".')


if __name__ == "__main__":
    main()
