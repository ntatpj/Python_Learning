# def ()
strg = input ("Enter the IP address")
list = strg.split(".")
# print(list)
# list = ["25","22","34","43"]
try:
    int_list = [int(i) for i in list]
except:
    print("enter integers only")
# print(int_list)
# a =12
# print(type(a))
# print(type(int_list[0]))
for o in int_list:
    if 0 < o <= 255 :
        flag = True
    else:
        flag = False
        break
if flag == True:
    print("valid IP address")
elif flag == False:
    print("Invalid IP adr")