from random import randint
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

real_num = randint(a, b)

i = 0
while True:
    try:
        guess_num = int(input('Please input a number 1-10: '))
        if real_num == guess_num:
            print('Awesome, you are the winner')
            break
        elif i < 5:
            print('Please try again')
        else:
            print('Sorry, you have reached the maxium number of try. You lost.')
            break
    except ValueError:
        print('Seems you didn\'t type a number, try again')
        continue

    i += 1
    
    