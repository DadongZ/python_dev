#dict keys has to be always immutable, unique
user = {
    'basket': ['apple', 'books', 'pens'],
    'greet': 'Hello'
}

print(user.get('age')) #get None
print(user.get('age', 55)) #if age exist print else if doesn't exist use 55

print('greet' in user.keys())
print(user.items())
print('Hello' in user.values())

user1 = user.copy()
print(f'user1 is {user1}')

print(f'random rm, {user1.popitem()}') #redomly pop up because dict is not ordered
print(f'new user1 {user1}')

#print(user['age']) #get error

user2 = dict(name='Alex Zhang', gender="male")
print(user2)