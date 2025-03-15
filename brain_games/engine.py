import sys

def run_game(game_logic, game_instruction):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_instruction)

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip().lower()

        if str(answer) == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            sys.exit()

    print(f"Congratulations, {name}!")
