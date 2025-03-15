import random

from brain_games.scripts import interface


def generate_progression():
    length = random.randint(5, 10)
    difference = random.randint(1, 5)
    start = random.randint(1, 10)
    progression = [start + i * difference for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."
    return progression, correct_answer


def play_progression_game():
    name = interface.start_game()

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        progression, correct_answer = generate_progression()
        print("Question:", " ".join(map(str, progression)))

        answer = input("Your answer: ").strip()

        correct_answers += interface.check_answer(answer, correct_answer)

    print(f"Congratulations, {name}!")


def main():
    play_progression_game()


if __name__ == "__main__":
    play_progression_game()
