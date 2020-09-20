# four pillars of oop
#1 encapsulation: binding data type and functions
#2 abstraction: giving access to only what's necessary
### private vs public variable: use underscore for private such as self._name (but no guarantee)
#3 inheritance: allows new objects to take on the properties of existing objects.
#4 polymorphism: the way in which object classes can share the same method name but these names can act differently based on what obect calls now.

class NameOfClass():
    class_attribute = 'value' #global attributes

    def __init__(self, param1, param2):
        self.param1 = param1 #object attributes
        self.param2 = param2

    def method(self):
        pass

    @classmethod
    def cls_method(cls, parameter_list):
        pass

    @staticmethod
    def stc_method(parameter_list):
        pass

#introspection: the ability to determine the type of an object at runtime