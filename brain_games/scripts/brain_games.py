import random
from brain_games.engine import run_game


def game_logic():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(["+", "-", "*"])

    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)

    return question, correct_answer


def main():
    run_game(game_logic, "What is the result of the expression?")


if __name__ == "__main__":
    main()
