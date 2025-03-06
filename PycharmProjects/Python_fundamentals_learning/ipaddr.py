lst1=[1,2,3,4,5,1,2]
leng = len(lst1)
print(leng)
new_list  = []
i = 0
while i<leng:

    if lst1[i] not in new_list:
        new_list.append(lst1[i])
#         pass
    i+= 1
print(new_list)
b = [54,34,9,0]
a = 9
# def funct(j):
#     while a not in j:
#         print("OK")
# k = map(funct,b)

a not in j