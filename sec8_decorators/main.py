#decorator: super boost functions, add extra functionality to other functions

## decorator pattern
def my_decorator(func):
    def wrap_func(*arg, **kwarg):
        print('-----------------------')
        func(*arg, **kwarg)
        print('-----------------------')
    return wrap_func


@my_decorator
def hello(greeting, emoji):
    print(f'Hi {greeting}{emoji}')

hello('good morning!', emoji=":)")


##example
from time import time
from functools import reduce

def performance(fn):
    def wrapper(*arg, **kwarg):
        t0 = time()
        result = fn(*arg, **kwarg)
        t1 = time()
        print(f'it took {t1-t0} seconds')
        return result
    return wrapper

@performance
def check_time(num):
    return reduce(lambda acc, i: acc+i*5, range(num))

print(check_time(5000000))


