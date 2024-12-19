import random


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
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        progression, correct_answer = generate_progression()
        print("Question:", " ".join(map(str, progression)))

        answer = input("Your answer: ").strip()

        if answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression_game()
