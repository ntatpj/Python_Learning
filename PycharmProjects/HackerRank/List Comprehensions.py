x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_major = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i + j + k != n:
                list_mini = [i, j, k]
                list_major.append(list_mini)
            else:
                pass
print (list_major)