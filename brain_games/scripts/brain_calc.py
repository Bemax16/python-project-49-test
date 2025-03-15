import random

from brain_games.scripts import interface


def calculate_expression(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2


def play_calc_game():
    name = interface.start_game()
    print('What is the result of the expression?')
    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice(["+", "-", "*"])
        print(f"Question: {num1} {operator} {num2}")
        answer = int(input("Your answer: "))

        correct_answer = calculate_expression(num1, num2, operator)

        correct_answers += interface.check_answer(answer, correct_answer, name)
    print(f"Congratulations, {name}!")


def main():
    play_calc_game()


if __name__ == "__main__":
    play_calc_game()
