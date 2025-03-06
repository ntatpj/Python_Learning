# print((lambda: 2 + 10)())
# print(x())
a =10
b=20
# print((lambda c,d:a+c,lambda d,c:b+d)[a<b](1,2))
x = ["print a = b " if(a==b)else  "a>b " if(a>b) else  "a<b"]
print(x)
print((lambda a:a+10)(5))