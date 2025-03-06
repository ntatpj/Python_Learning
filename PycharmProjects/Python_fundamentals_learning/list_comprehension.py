# to convert string array content in int

# a = ["23", "3", "5", "11"]
# a = [int(x)for x in a]
# print(a)
# # print([int(x) for x in a])
# print([pow(i,2) for i in a])

#to check IP address

stir = "5.255.255.-1"
a = stir.split(".")
a = [int(x) for x in a]
print(a)
for x in a:
    [print("IP is OKr") if 0 <= x <= 255 else print("reenter IP")]