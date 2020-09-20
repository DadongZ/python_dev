# Error Handling: allows us to let the python script continue running even if there're errors

while True:
    try:
        age = int(input('what is your age?'))
        print(10 / age)
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a none zero positive number')
        continue #go back to 'what is your age?'
    else:
        print(f'Your age is {age}. Thank you!')
        break
    finally: #regardless what happened this will print
        print('Okay, everything done!')


while True:
    try:
        age = int(input('what is your age?'))
        print(10 / age)
        raise ValueError('Hey you got value error!!')
    except ZeroDivisionError:
        print('Please enter a none zero positive number')
        continue #go back to 'what is your age?'
    else:
        print(f'Your age is {age}. Thank you!')
        break
    finally: #regardless what happened this will print
        print('Okay, everything done!')

def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)

print(sum("1", 2))
    
