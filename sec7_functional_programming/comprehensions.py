#list/set/dict comprehensions

## list = [param for param in iterable]
### example1
my_list = []

for i in 'Dadong Zhang':
    my_list.append(i)

print(my_list)

my_list1 = [x for x in "Dadong Zhang"]
print(my_list1)

###example2
a = [(0,2), (4,3), (10, -1), (9, 9)]

a2= list(map(lambda x: [x[1], x[0]], a))
a3= [(x[1], x[0]) for x in a]
a4= [(x[1], x[0]) for x in a if x[1]>0]

print(a2)
print(a3)
print(a4)


## dict = {key:value for key, value in dict0}
my_dict = {
    'd': 0,
    'a': 1,
    'b': 2,
    'c': 3
}

my_dict1 = {x: y**2 for x, y in my_dict.items() if y >0}

print(my_dict1)

my_dict2 = {x: x**2 for x in [1, 2, 3]}
print(my_dict2)

##ex, find duplicates
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

print(set([x for x in my_list if my_list.count(x)>1]))
