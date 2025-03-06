class Mother:
    def __init__(self):
        self.Mother ="Sakshi"
    def whoisparent(self):
        print(f"Mothers name is {self.Mother}")

class Father:
    def __init__(self):
        self.Father = "Ramlal"
    def whoisparent(self):
        print(f"Father name is {self.Father}")

class child(Father, Mother):
    def __init__(self):
        self.name = "Harush"
        print(self.name)
        # Mother.__init__(self)
        Father.__init__(self)
    # def whoisparent(self):
    #     print("I am orphan")

family = child()
family.whoisparent()
# print(child.mro())

