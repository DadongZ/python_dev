# nexted for loops
for item in (1,2,3,4,5):
    for x in 'abc':
        print(item, x)

# iterable: list, dict, tuple, set, string
my_list = range(0, 10, 2)
count=0
for i in my_list:
    print(i)
    count +=1

print(f'the length of {my_list} is {count}')

# enumerate
for i, c in enumerate('Dadong Zhang'):
    print(i, c)


# while
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

#while True:
#    response = input('say something: ')
#    if response=='bye':
#        break

#break, continue and pass
for c in 'alex zhang':
    print(c) #not print if put print below `continue` due to `continue` will loop back to for loop.
    continue
#pass usually used for placehold
for i in my_list:
    pass