#parent class
class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')
    
#children/sub/derived classes: Wizard, Archer
class Wizard(User):
    def __init__(self, name, power, email):
        #User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

wz1 = Wizard('Alex', 10, "axzhang2@gmail.com")

wz1.sign_in()
print(wz1.email)

#introspection: the ability to determine the type of an object at runtime
print(dir(wz1)) #all methods and attributes that Wizard instants have
