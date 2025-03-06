class Mother:
    age = 78
    def __init__(self):
        self.Mother = "Sakshi"
    def whoisparent(self):
        age = 90  #Note calling this variable of parent "class" method is not possible becase exixtance of attributes og method starts with method and ends with method
        print(f"Mothers name is {self.Mother}")

class Father:
    def __init__(self,age):
        self.Father = "Ramlal"
        self.age = 98
        print("you have access init of Father class")
    def whoisparent(self):
        print(f"Father name is {self.Father}")
    def met(self):
        print("this is method in Father class")

class child(Father,Mother):
    def __init__(self):
        super().__init__(88)      ##this super will initialize constructor of fist parent clas name argument only;  # hence in this cas, Father class constructor is not initalised unless and until specified explicitly
        # Father.__init__(self,909)
        self.name = "Harush"
        print(self.name)
        print(Mother.age)



family = child()
family.whoisparent()
print(child.mro())
family.met()

#NOte, super() does not require "self" as argument; it requires all other arguments in class.
#Classname does require "self"+other arguments in class