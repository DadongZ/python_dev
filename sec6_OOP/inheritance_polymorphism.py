#USERS
##-Wizards
##-Archers
##-Hunters
##all have to sign in

###exmaple1
class SuperList(list):
    def __len__(self):
        return 1000
    
sp1 = SuperList()
sp1.append(5)

print(issubclass(SuperList,list))
print(issubclass(list, object))


###example2
#parent class
class User():
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('Do Nothing')

#children/sub/derived classes: Wizard, Archer
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    
    def attack(self):
        print(f'attacking with arrows left {self.arrows}')

    def run(self):
        print('run very fast') 

wz1 = Wizard('Alex', 10)
ar1 = Archer('Halley', 18)
# both share sign_in()

wz1.sign_in() #inherited from class User
wz1.attack()
ar1.attack()


## check if something an instance of a class

#isinstance(instance, class)

print(isinstance(wz1, Wizard))
print(isinstance(wz1, object)) #from `object` base class to access __method__


#polymorphism
#both Wizard and Archer share method attack() but they are different meaning for each object

def player_attack(char):
    char.attack()

player_attack(wz1)
player_attack(ar1)

##example3 multi inheritance

class HybridBorg(Wizard, Archer): #inherit Wizard first then Archer
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

hb1 = HybridBorg('Alex', 50, 100)

print(hb1.run())
print(hb1.power)
print(hb1.arrows)
