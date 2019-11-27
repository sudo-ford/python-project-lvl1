import prompt
import random


def run():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    counter = 0
    while counter < 3:
        count = 0
        number = random.randint(0, 50)
        question = ''
        step = random.randint(1, 9)
        random_dots = random.randint(0, 9)
        answer = None
        while count < 10:
            if count == random_dots:
                question += ' ..'
                answer = str(number)
            else:
                question += ' ' +  str(number)
            number += step
            count += 1
        print('Question: ' + question)
        your_answer = prompt.string('Your answer: ')
        if your_answer == answer:
            print('Correct!')
            counter += 1
        else:
            print(str(your_answer) + " is wrong answer ;(. Correct answer was " + answer + '.\n' + "Let's try again, " + name + "!")
    print("Congratulations, " + name + "!")
