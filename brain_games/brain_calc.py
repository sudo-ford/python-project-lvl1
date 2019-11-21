import prompt
import random


def run():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    count = 0
    while count < 3:
        number_1 = random.randint(1, 99)
        number_2 = random.randint(1, 99)
        operators = ['+', '-', '*']
        operator = random.choice(operators)
        print('question: ' + '{} {} {}'.format(number_1, operator, number_2))
        result = 0
        if operator == '+':
            result = str(number_1 + number_2)
        elif operator == '-':
            result = str(number_1 - number_2)
        else:
            result = str(number_1 * number_2)
        answer = prompt.string('Your answer: ')
        if result == answer:
            print('Correct!')
            count += 1
        else:
            print(str(answer) + " is wrong answer ;(. Correct answer was " + str(result) + '.\n' + "Let's try again, " + name + "!")
    print("Congratulations, " + name + "!")
