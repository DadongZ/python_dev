# Fundamental data types
int
float
bool
str
list #like array, list of items or values
set
tuple
dict
complex #probably never use
print(bin(5)) 
print(int('0b101', 2))

# Classes -> custom types

# Specialized data types
##modules

None #absent of value

# Expressions vs Statements
iq = 100
user_age = iq / 5
# Expression produce value: `iq/5`
# statement: `user_age = iq / 5`  
# augmented assignment operator some_value +=2 
# Escape sequence: double and single quote, weather ="it\"s sunny"
print("\tIt's \"kind of \" sunny\n")

# formated string
name = 'Dadong Zhang'
age = 42
print(f'hi {name}. You are {age} years old')
print('hi {0}. You are {1} years old'. format(name, age))
print('hi {1}. You are {0} years old'. format(name, age))
print('hi {nm}. You are {ag} years old'. format(nm="Alex", ag=10))

# immutability
selfish='01234567'
# selfish[0]='8' -> error strings are immutable

birth_year = input('what year were you born?')
age = 2019 - int(birth_year)

print(f'your age is: {age}')
