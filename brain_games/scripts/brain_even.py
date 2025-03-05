import random


def is_even(number):
    return number % 2 == 0


def play_even_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if answer == correct_answer:
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
    play_even_game()


if __name__ == "__main__":
    play_even_game()
