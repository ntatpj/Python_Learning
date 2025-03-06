class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self,name, breed):
        # Animal.__init__(self, name, species="Cat")
        self.name = name
        self.breed = breed

#the Dog class has its own __init__ method that adds a new attribute for the breed of the dog,
#and it also overrides the make_sound method to specify the sound that a dog makes.
    #make sound method is overriden by methosm in shil_clas
    def make_sound(self):
        print("Bark!")

# class Cat(Animal):
#     def __init__(self, name, house):




d = Dog("Dog", "Doggerman")
print(d.make_sound())

a = Animal("Tiger","Cat")
print(a.make_sound())