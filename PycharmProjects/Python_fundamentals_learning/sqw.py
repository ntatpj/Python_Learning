import copy

a = [312,3112]
print(type(a))
b = a
print(id(a))
print(id(b))

c = [231,243,"dfds"]
d = copy.copy(c)
print("c is",id(c))
print("d id shllaow copy of c",id(d))

e = ["adsdas",213]
f = copy.deepcopy(e)
print(id(e))
print(id(f))
