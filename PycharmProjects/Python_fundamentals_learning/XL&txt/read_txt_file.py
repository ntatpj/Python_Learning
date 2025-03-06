f =open("C:/Users/ntatpuj/Desktop/pypy.txt")
# print(f.tell())
# print(f.readline())
# print(f.readline())
# f.seek(0)
# print(f.readline())
word = "GIL"
while True:
    line = f.readline()
    if line == "":
        break
    # print(line)
    # f.tell()
    if word in line:
        print("YEs")
f.close()



# f_org = f
# print("org is1",f_org.tell())
# print(f.readline())
# print(f.tell())
# print("org is2",f_org.tell())
# f = f_org
# print("org is3",f_org.tell())
# print(f.tell())
# print(f_org.readline())
