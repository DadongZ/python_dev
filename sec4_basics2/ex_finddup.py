my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

dup_list = []

for i in my_list:
    if my_list.count(i) > 1:
        idx = my_list.index(i)
        if i not in dup_list:
            dup_list.append(my_list[idx])


print(dup_list)
