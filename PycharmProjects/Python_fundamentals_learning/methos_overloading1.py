class A:
    print(dir(int))
    def sum(self,a=0,b=0,c=0):
        x = a+b+c
        print(x)


l = A()
l.sum(10,20)
dir(int)