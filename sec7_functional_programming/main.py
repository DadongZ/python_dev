def multiply_by2(ls):
    new_ls = []
    for item in ls:
        new_ls.append(item*2)
    return new_ls

# print(multiply_by2([1,2,3]))

# pure function
## always generate same output
## nothing in the outside world matters to this function
## return print(new_li) will have side effect because using print statement


# map(action, )
def multiply2(item):
    return item*2
print(list(map(multiply2, [1,2,3,4])))

# filter()
def only_odd(item):
    if item % 2 !=1:
        return item
print(list(filter(only_odd, [1,2,3,4,5,6])))

# zip()
users = ["Alex", "Dadong", "Halley", "Daisy"]
ids = [";lakd", "ja;lkd", "ae;lkas", ";aksdf;alsk"]
emails = ['abc@gmail', "akd@hot", "alkjd@duke", "lta@nccu"]
print(list(zip(users, ids, emails)))

# reduce()
from functools import reduce
def accumulator(acc, item):
    print(acc, item)
    return acc * item     

my_list = [1, 2, 3, 4, 5, 6]
print(reduce(accumulator, my_list, 2))

# lambda: one time anonymouse functions
##example1
print(list(map(lambda item: item*2, my_list)))

##example2
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9] 
print(list(map(lambda x, y, z : x+y+z, a, b, c)))
print(reduce(lambda acc, item: acc*item, my_list))

##example3
a = [(0,2), (4,3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1]) #sort by second values
print(a)
