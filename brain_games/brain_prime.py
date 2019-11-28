import prompt
import random
import math


def run():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    count = 0
    while count < 3:
        number = random.randint(2, 99)
        i = 2
        answer = ''
        limit = int(math.sqrt(number))
        while i <= limit:
            if number % i == 0:
                answer = 'no'
                break
            else:
                answer ='yes'
            i += 1
        print('Question: ' + str(number))
        your_answer = prompt.string('Your answer: ')
        if your_answer == answer:
            print("Correct!")
            count += 1
        else:
            print(your_answer + " is wrong answer ;(. Correct answer was " + answer + '.\n' + "Let's try again, " + name + "!")
    print("Congratulations, " + name + "!")
