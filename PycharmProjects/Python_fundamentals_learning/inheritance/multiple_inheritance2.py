#Inheritance without calling parent class constructor and defining parent class attributes as local attributes

class Mother:
    def __init__(self,momname):
        self.Mother = momname
    def whoisparent(self):
        print(f"Mothers name is {self.Mother}")

class Father:
    def __init__(self,fatname):
        self.Father = fatname
    def whoisparent(self):
        print(f"Father name is {self.Father}")

class child(Mother,Father):
    def __init__(self, momname, fatname, myname):
        self.name = myname
        self.Father = fatname
        self.Mother = momname
        print(self.name)
        # Mother.__init__(self,momname)
        # Father.__init__(self,fatname)

family = child("Sakshi", "Ramlal", "Harush")
family.whoisparent()
print(child.mro())

