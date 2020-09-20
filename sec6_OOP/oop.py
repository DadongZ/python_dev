#1. What is Object oriented programming
# object: objects have methods and attributes that you can access with DOT metho.
# class: blueprint/building block -> instantiate different instances/objects over and over

class PlayerCharacter:
    #Class object Attribute, not dynamic, it's static
    membership = True
    #self refers to PlayerCharacter
    def __init__(self, name="anonymous", age=0):
        #if (PlayerCharacter.membership): either way is working because self<->PlayerCh
        if (age > 18):
            self.name = name #this regular attribute is dynamic
            self.age = age #property

    def shout(self): #method shout
        print(f'My name is {self.name}') 
        #cannot use PlayCharacter.name because PlayCharacter does have attribute name (only membership attribute).
    
    #decorator
    @classmethod #access instanciate
    def adding(cls, num1, num2): #cls refers to PlayerCharacter class
        return cls("Alex", num1 + num2) #instaciate within classmethod

    @staticmethod #no access to cls
    def addings(num1, num2): #cls refers to PlayerCharacter class
        return num1 + num2 #instaciate within classmethod

    

player1 = PlayerCharacter('Cindy', 22) #player1 has attribute name Cindy
print(f'{player1.name} is {player1.age} years old')
player1.shout()
print(player1.membership)

player2 = PlayerCharacter.adding(2,20) # has to be greater than 18

print(player2.name)