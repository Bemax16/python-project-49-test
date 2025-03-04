import random


def calculate_expression(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2


def play_calc_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice(["+", "-", "*"])
        print(f"Question: {num1} {operator} {num2}")
        answer = input("Your answer: ").strip()

        correct_answer = calculate_expression(num1, num2, operator)

        if answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    play_calc_game()


if __name__ == "__main__":
    play_calc_game()
