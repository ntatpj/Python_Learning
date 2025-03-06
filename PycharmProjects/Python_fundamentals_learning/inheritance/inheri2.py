class People():
    count = 0 //2
    num = 0
    name = "o"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        People.count += 1 //1 //2
        self.num += 1 //1 //1

    def countofPeople(self):
        print("self.count is {0}" .format(self.count))
        print("People.count is " , People.count)

    def details(self):
        print("self.num is" ,self.num)
        print("People.num is", People.num)

#
# rohit = People("Rohit",28)
# rohit.details()
# rohit.countofPeople()
#
# samantha = People("Samantha" ,8)
# samantha.details()
# samantha.countofPeople()


class Employee(People):
    def __init__(self,company,post):
        super().__init__("sank", 34)
        self.company = company
        self.post = post
    def printEMPdetails(self):
        print(People.name)


swati = Employee("Google", "virtualization Engg")
print (swati.company)
print (swati.post)
print (swati.name)

swati.printEMPdetails()