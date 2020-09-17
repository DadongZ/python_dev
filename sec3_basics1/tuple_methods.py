#dict items are tuple
user = {
    'basket': ['apple', 'books', 'pens'],
    'greet': 'Hello'
}

print(user.items())

my_tuple =(1,2,3,4,5)
new_tuple = my_tuple[1:2]
x,y,z, *other = (1,2,3,4,5)
print(new_tuple)
print(x)
print(other)

print(my_tuple.count(3))
print(my_tuple.index(3))

