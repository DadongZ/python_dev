# iterable: object that can loop through, dunder method __iter__
# generator: function that generates iterable object

#under hood
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break

special_for([1,2,3,4])


#ex: fibonacci number
from functools import reduce
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a=b
        b=temp+b

[print(x) for x in fib(20)]



#example
def generator_function(num):
    for i in range(num):
        yield i**2
        #yield() pauses the functions and come back to it when next() called

for item in generator_function(10):
    print(item)

g = generator_function(100)
print(g)
next(g)
next(g)
next(g)
print(next(g))
#until reached the end of num

#revisit performance
from time import time
def performance(fn):
    def wrapper(*arg, **kwarg):
        t0 = time()
        result = fn(*arg, **kwarg)
        t1 = time()
        print(f'it took {t1-t0} seconds')
        return result
    return wrapper

@performance
def lt1(num):
    print('perform1')
    for i in range(num):
        i*5

@performance
def lt2(num):
    print('perform2')
    for i in list(range(num)):
        i*5

num = 1000000
lt1(num) #performs better
lt2(num)

