class people:
    count = 0
    num = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        people.count += 1
        self.num += 1

rohit = people("Rohit", 23)


print(people.count, rohit.count)
print(people.num, rohit.num)

swati = people("Swati",33)
print(people.count, swati.count)
print(people.num, swati.num)