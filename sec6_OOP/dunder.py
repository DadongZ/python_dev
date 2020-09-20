class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict={
            'name': 'yoyo',
            'age': 45
        }
    def __str__(self): #not suggested by you can modify the dunder method
        return f'{self.color}'

    def __len__(self):
        return 5
    
    def __call__(self):
        return 'yess??'
        
    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['age'])