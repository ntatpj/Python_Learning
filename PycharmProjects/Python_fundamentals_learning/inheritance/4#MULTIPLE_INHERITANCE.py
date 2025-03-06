# Multiple inheritance allows a class to inherit attributes and methods from multiple parent classes.
# This can be useful in situations where a class needs to inherit functionality from multiple sources.
# https://www.codewithharry.com/videos/python-100-days-of-code-79/


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")
        
    def show(self):
        print("I am in Anilmal_parent class")

class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
    def show(self):
        print("I am in Mammal parent class")

class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed

    def make_sound(self):
        print("Bark!")

    # def show(self):
    #     print("I am in child class")

d =Dog("Cat", "West_bengal_Loioness","Orange")
print("breed, child class attribute:", d.breed)
print("fur color, second parent class attribute:", d.fur_color)
print("this attribute is in both parent class, but it should chose animal as it is first attribute:", d.name)
print("Parent class first attribute:", d.species)
print("Child class attribute:", d.make_sound())
print(Dog.mro())
#MRO : Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes.
# The MRO determines the order in which parent classes are searched for attributes and methods.
#uncomment show in child class also and check
print(d.show())