class classA:
    u = 28
    def __init__(self):
        print("Welcome to classA")
        self.objA2 = "I am objectA2 of classA"  #so self.objA2 is instance variable becuse it is witin a constructor)

    v = 99
    
    def functA3(self,var):
        print("I am functA3 of classA")
        print("A2 is object of classA", self.objA2,var)
        print(self.u)



A = classA()
# B= classA()
# print(A.objA2)
A.functA3("A")
# B.functA3("B")
# print(classA.u)