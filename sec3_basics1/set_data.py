#set: unordered collections of unique objects

my_set = {1,2,3,4,5,6,6,6}
print(my_set)
my_set.discard(6)
print(my_set)


my_list=[1,2,3,4,5,5,6,6,7,7,8,8]
my_unique=set(my_list)
print(my_unique)
print(list(my_unique))
#print(my_unique[0]) error


my_set = {1,2,3,4,5}
your_set = {1,2,3,4,5,6,7,8,9,10}

print(my_set.difference(your_set))
print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set)) #nothing in common
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))
print(my_set.union(your_set))


my_set.difference_update(your_set)
print(my_set)