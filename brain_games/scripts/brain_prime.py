import random
from brain_games.engine import run_game


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def game_logic():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"

    return number, correct_answer


def main():
    run_game(game_logic, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == "__main__":
    main()
