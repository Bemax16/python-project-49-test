import random

from brain_games.scripts import interface


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def play_prime_game():
    name = interface.start_game()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_prime(number) else "no"

        correct_answers += interface.check_answer(answer, correct_answer, name)

    print(f"Congratulations, {name}!")


def main():
    play_prime_game()


if __name__ == "__main__":
    play_prime_game()
