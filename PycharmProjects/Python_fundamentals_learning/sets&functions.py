a = {1,3,78,2}
b = {1,3,31}

print(dir(a))
# print(a.add(80))
# print(a.difference(b))
# a.difference_update(b)
print(a)  # a={2,78,80}
# a.intersection_update(b)
# print(a)
# print(a.intersection(b))
# print(a)
# print(a.isdisjoint(b))
print(b.issubset(a))
a.update(b)
print(a)
a.i