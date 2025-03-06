# code
class Person:
    _name = "ok"
    # Constructor
    def __init__(self, id):
        # self.name = "Gogo"
        self.id = id
        self.just_a_name = "keerti"

    # To check if this person is an employee
    def Display(self):
        self.dada = "DeeK"


class Emp(Person):

    def __init__(self,sank, id):
        super().Display()
        self.sank = sank
        self.id = id

    print("Internal accing ofparent class memeber by class class member", Person._name)
    # print("Internal accing ofparent class memeber by class class member", Person.just_a_name )

Emp_details = Emp("Mayank", 103)

# calling parent class function
print(Emp_details.sank)
print(Emp_details._name)
print(Emp_details.id)
print(Emp_details.dada)
