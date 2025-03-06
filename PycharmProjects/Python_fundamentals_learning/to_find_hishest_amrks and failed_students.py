# details = {"Rahul": 99, "NEha": 90, "Jingo": 980}
# # print(details["Rahul"])
# # details["Sanket"]=(90)
# # print(details)

details = {}

name = "ok"
while name != "done":
    name = input("Enter the name")
    if name == "done":
        break
    Marks = int(input("Enter marks"))
    details[name]=(Marks)
print(details)

l = len(details)
# print(l)
#
#
# x = list(details.values())
# print(x.sort)
# print(x)


KEY = list(details.keys())
VAL = list(details.values())
print(KEY)
print(VAL)


Check_key_highest = "None"
Check_val_highest = 0
fail_list=[]

# print(KEY[1])
# print(details[KEY[0]])
for i in range(l):
    if details[KEY[i]] > Check_val_highest:
        Check_val_highest = details[KEY[i]]
        Check_key_highest = KEY[i]
    if details[KEY[i]] < 40:
        fail_list.append(KEY[i])

print(Check_key_highest)
print(Check_val_highest)
print(fail_list)

