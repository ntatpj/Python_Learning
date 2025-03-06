class A:
        classvar1 = "I am class variable of class A"
    def __init__(self):
        self.classvar1 = "I am instance varibale of class A"

    def result(self,a,b):
        print("Mul of 2 nos is:", a*b)

class B(A):
    classvar1 = "I am class variable of class B"

    def __init__(self):
        super().__init__()
        pass
        self.classvar1 = "I am instance varibale of class B"

    def result(self,a,b):
        pass

        print("Sum of 2 nos is:", a+b)
        super().result(a, b)

a = A()
b = B()
print(b.classvar1)
b.result(10,20)

# First it will check if there is :classvar1 instance variable in class B,
# then it will check classvar1 instance variable in class A,
# then it will check classvar1 class variabl in class B,
# then it will check classvar1 class varable in class A.