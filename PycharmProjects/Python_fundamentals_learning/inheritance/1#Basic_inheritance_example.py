class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        # print("I have access to init of Employe")
    def showDetails(self):
        print("Name of employee is {0} and his id-no is {1}".format(self.name,self.id))
#
# emp = Employee("Rohan Das" , 420)
# emp.showDetails()

# NOW I want to add details of a programer aswell, a programmer is also an employee but has his own features like programing language he know

class Programer(Employee):
    def showLanguage(self):
        print("The default language is Python")

prog = Programer("Jack",9090)
prog.showLanguage()
prog.showDetails()
print(prog.name)
print(prog.id)

# INHERITANCE: Isme child class apne parent class ki saari properties ko inherit kr sakta hai [def __init__(self, name, id) & def showDetails(self)],
# Child class inherits all the behaviour and propertis of parent class including __init__method and showDetails method.
# additionally, child class has it's own __init__ method that adds it's new attribute for the child class. And it alo overrides
# make sound method to specify the dound that the dog makes.
# lekin iske alawa child class ki apni alg se bhi properties hoti hai[showLanguage(self)]