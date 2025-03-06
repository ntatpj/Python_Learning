class Test:
    name = "kjl"
    num = 0
    def __init__(self,name,age):
        self.name = name
    def pri(self):
        print(self.num)
        kla = 32

class tumtum(Test):

    def __init__(self,name,age):
        Test.__init__(self,name,age)
        # super().__init__(name,age)
        self.name_ = name
        print(self.num)
    def gri(self):
        print(self.name)


obj = tumtum("Sank" , 34)
print(obj.num)
print(obj.name_)
print(obj.name)
obj.gri()