a = [10,20,30,40]
b = [5,15,25,39]
x = []
# for i in range(min(len(a),len(b))):
#     x.append(a[i]-b[i])

# for i,j in zip(a,b):
#     x.append(i-j)


[x.append(a[i]-b[i]) for i in range(min(len(a),len(b)))]

print(x)
