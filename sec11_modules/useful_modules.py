from collections import Counter, defaultdict, OrderedDict
import datetime 
from array import array

# Counter: count frequence of each element

lst = [1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6]

print(Counter(lst))

sentence ='Cockroaches are insects of the order Blattodea, which also includes termites. About 30 cockroach species out of 4,600 are associated with human habitats. About five species are well known as pests.'

print(Counter(sentence))

# defaultdict insert callable value if not exist
dct = defaultdict(lambda: 'does not exist', {
    "a": 1,
    "b": 2,
    "d": 4
})

print(dct['c'])

#OrderedDict: retains the order that you insert into a dictionary

od1 = OrderedDict()
od1['a'] = 1
od1['b'] = 2

od2 = OrderedDict()
od2['b'] = 2
od2['a'] = 1

print(od1 == od2) #False

#time
print(datetime.time(5, 45, 2))
print(datetime.date.today())

#array
arr = array('i', [1,2,3])

print(arr)