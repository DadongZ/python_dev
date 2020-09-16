amazon_carts =[
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_carts[0] = "laptop"
print(amazon_carts.append('printer'))
print(amazon_carts.extend('printer'))
print(amazon_carts.pop())
print(amazon_carts.insert(5, "cups"))
print(amazon_carts.remove("toys"))
print(amazon_carts.index("r"))
print(amazon_carts.count("n"))

matrix = [
    [1,2,3],
    [2,3,4],
    [7,8,9]
]
print(matrix[1][0])
print(len(matrix))

sorted(amazon_carts) #create new variable
amazon_carts.sort() #change variable itself


print(list(range(100)))

newjoin = ' '.join(['Hi', 'my', 'name', 'is', 'Alex'])

#list unpacking
a,b,c, *others, d= range(20)
print(a)
print(b)
print(c)
print(others)
print(d)
