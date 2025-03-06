
#If there are two methods of same name, thne which method will be called will depend on what agrument is given.
# Depending on argument number the method is choosen
# if the number of argument is also same, then it will call the latest function.
class A:

    def sum(self):
        print("I am khali pili")

    def sum(self,a):
        print("sum is", a)





p = A()
# p.sum(10)
p.sum()