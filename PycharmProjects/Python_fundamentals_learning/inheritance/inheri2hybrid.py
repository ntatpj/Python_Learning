class Fruits:
    _favourite = "Apple"

    # non-parameterized constructor
    def __init__(self):
        kj = 89
    #  Protected: ‘_’ symbol before the data member of that class.
    def __put(self):
        self.favourite = "Orange"

    def presh(self):
        print(self.freshies == "Kiwi")

    # a method

    # def show(self):
    #     print(self.favourite)

class Ediblefruits(Fruits):
    huhu = "My tummy!"

    def __init__(self,huhu):
        print("J for Jackfruit")

    def cut(self):
        print("to cut fruit", self._favourite)


class vegiFruits(Fruits):
    gogo = "Yummy!"
    def __init__(self):
        print("You can serve healthy", self._favourite)

# creating an object of the class

class Jumboplate(vegiFruits):
    def __init__(self):
        print("I am final product of vegi & Edi" , vegiFruits.gogo)

    def soleparent(self):
        print(Fruits._favourite)




obj = Jumboplate()
obj.soleparent()
print(obj.presh())

# calling the instance method using the object obj

