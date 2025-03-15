import random

from brain_games.scripts import interface


def is_even(number):
    return number % 2 == 0


def play_even_game():
    name = interface.start_game()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        correct_answers += interface.check_answer(answer, correct_answer, name)

    print(f"Congratulations, {name}!")


def main():
    play_even_game()


if __name__ == "__main__":
    play_even_game()
