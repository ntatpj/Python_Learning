class Employee:
    def __init__(self, name, id):
        self._name = name
        self.__id = id
        # print("I have access to init of Employe")
    def showDetails(self):
        print("Name of employee is {0} and his id-no is {1}".format(self._name,self.__id))
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
print(prog._name) #_name is  a protected member of parent class, hecne accessible by onject of child class
print(prog.__id)    #__id is privte member of parent class, hence not recognized by child class object