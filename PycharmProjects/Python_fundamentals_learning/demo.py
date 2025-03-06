class People:
    count = 0
    num = 0
    list_of_names = []
    def __init__(self, name , ages):
        self.name = name
        self.age = ages
        print(f"My name is {self.name} & my age is { self.age}")
        People.count += 1
        self.num +=1
        People.list_of_names.append(self.name)
        print(People.list_of_names)


Rahul = People("Rahul Rastogi", 22)
print(Rahul.count)
print(People.count)
print(Rahul.num)
print(People.num)
Swati = People("Swati Sahu", 98)
print(Swati.count)
print(People.count)
print(Swati.num)
print(People.num)