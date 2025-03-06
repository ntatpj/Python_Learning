class classA:
    _kko = 98
    def __init__(self):
        print("Welcome to classA", self._kko)
        self.sanket = "bF"
    #
    # def funct2A(self):
    #     print("OK FINE")
    #     print("I am functu 2 of A Calaaass" , _kko)

    objA2 = "I am objectA2 of classA"
    opj = _kko
    def functA3(self):
        return("I am functA3 of classA",self._kko, self.sanket)



class classB(classA):
    mko = 90
    def __init__(self):
        print ("nko = 99")
        lko = 109   #why is thi obj not printed for print(B.lko)

    objB = 78
    def _functuB(self):
         print("Ob A ka private", self._kko)

A = classA()
B = classB()
# print(B.funct2A())
print(B.objB)
print(B.mko)
print(B.functA3())
print(B.opj)
print(B._functuB())
print(B._kko)

