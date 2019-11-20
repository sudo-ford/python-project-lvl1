import prompt
import random


def run():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    count = 0
    while count < 3:
        rand = random.randint(1, 99)
        print("Question: " + str(rand))
        answer = prompt.string('Your answer: ')
        flag = rand % 2
        if flag:
            if answer == 'no':
                print('Correct!')
                count += 1
            elif answer == 'yes':
                print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + "!")
            else:
                print("Incorrect answer. Please answer 'yes' or 'no'")
        else:
            if answer == 'yes':
                print('Correct!')
                count += 1
            elif answer == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + name + "!")
            else:
                print("Incorrect answer. Please answer 'yes' or 'no'")
    print("Congratulations, " + name + "!")
