# Data members of a class are
# declared protected by adding a single underscore ‘_’ symbol before the data member of that class.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def parents(self):
        print("Name of mychil is {0} and his age is {1}".format(self._name , self._age))

obj = Person("Rahul",8)
obj.parents()
obj._name = "Prachi"
obj.parents()


print(Person.__dict__)