dic = {(0,1):"ok", (9,8):"lki",(2,1):"ujja"}
# mict = {[0,2]:"jji",[2,1]:"LoLO"}

# print(dic[(9,8)])
#
# tup = (12,2,1,32)
# print(tup[0])
print(dir(dic))
print(dic.copy())

p = {1000:23,2:21,221:3}

print(p.items())
print(dic.keys())
x = list(p.keys())
print(x)
x.sort()
print(x)
print(p.get(1000))
print(p[1000])
p.popitem()
print(p)
p.pop(1000)
print(p)
print(p.values())
print(p)
f = p.setdefault(1000,13)
f= p.setdefault(1000,34)
print(f)
p.update({90:232})
print(p)
print(p.clear())
print(p)

