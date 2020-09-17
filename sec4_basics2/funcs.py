#1. parameters vs arguments
# parameters: defined in a function
# arguments: the actual values when we call/envoke a function

def say_hello(name, emoji):
    print(f'Hello {name}{emoji}')

#2. positional arg vs keywords arg
# positional arg: arg require at the proper position/order
# keywords arg: arg require at the proper position/order
say_hello('Dadong', '😍')

say_hello(emoji='😍', name="Dadong")

# excercise
def checkDriverAge(age):
    if int(age) < 18:
	    print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
	    print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
	    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(92)

#3. method vs function
# functions: list(), print(), max(), min(), input(), customize def
# methods: methods owned by an object and using by '.' notation.


#4. docstrings
def test(a):
    '''
    Info: this function tests and prints docstring
    '''
    print(a)
help(test)
print(test.__doc__)

#5. *arg vs. **kwarg

def super_func(args):
    return sum(args)
#super_func(1,2,3,4,5) TypeError supper_func take 1 positional argument 5 were given

def super_func(*args):
    '''
    '*arg' accept any number of arguments
    '''
    print(args)
    return sum(args)
super_func(1,2,3,4,5)

def super_func(*args, **kwargs):
    '''
    '*arg' accept any number of arguments\n
    '**kwarg' accept key works arguments
    '''
    total = 0
    print(args)
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=20))
#RULE: params, *args, default parameters, **kwargs
def super_func(name, *args, greet="Hello", **kwargs):
    pass

#ex find the hight even number
def highest_even(li):
    ev = []
    for i in li:
        if i%2 == 0:
            ev.append(i)
    return max(ev)

print(highest_even([10,2,3,4,5,8,11, 16, 21]))


#6. Scope: what variable do I have access to.
#RULE: (1) start with local -> (2) parent local -> (3) global -> (4) build in python functions.
total = 10 #global scope

def test():
    total = 100 #only access within the def
    return total
print(total)
print(test())

#global
total = 0

def count():
    global total
    total += 1
    return total
count()
count()
print(count())

#better way Dependency injection
total = 0
def count2(total):
    total += 1
    return total
print(count2(count2(count2(total))))


#nonlocal: refers to parent local
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner: ', x)

    inner()
    print('outer:', x)

