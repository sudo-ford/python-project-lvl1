import prompt
import random


def run():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    count = 0
    while count < 3:
        number_1 = random.randint(1, 99)
        number_2 = random.randint(1, 99)
        print('Question: ' + '{} {}'.format(number_1, number_2))
        while number_1 != 0 and number_2 != 0:
            if number_1 > number_2:
                number_1 %= number_2
            else:
                number_2 %= number_1
        gcd = str(number_1 + number_2)
        answer = prompt.string('Your answer: ')
        if gcd == answer:
            print('Correct!')
            count += 1
        else:
            print(str(answer) + " is wrong answer ;(. Correct answer was " + str(gcd) + '.\n' + "Let's try again, " + name + "!")
    print("Congratulations, " + name + "!")
