
#1 true or false
password = '123'
username = 'JohnJohn'

if password and username:
    print('You\'re logged in')
else:
    print('You\'re logged out')

#2 ternary operator
## condition_if_true if condition else condition_if_else

is_Friend = True
can_message = "message allowed" if is_Friend else "not allowed to message"

print(can_message)

#3 short circuiting
is_Friend = False
is_User = True

#x or y, if x is False then y, else x
if is_Friend or is_User:
    print('best friends')
#x and y, if x is false then x else y
if is_Friend and is_User:
    print('and best friends')


#4 logic operators
# >, <, ==, or, and, in, !=

# different between is and ==
print(True == 1)
print(True is 1)
print([] == [])
print([] is []) #False, they are two complete different lists in different locations in mem.
print([1,2,3] is [1,2,3]) #False, they are two complete different lists in different locations in mem.
print([1,2,3] == [1,2,3]) #True because it only checks values