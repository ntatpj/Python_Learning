import re
f = open("C:/Users/ntatpuj/Desktop/scripts_small/NVM_legal_illegal.txt")
print(re.search("model",f))
text = "It often rains in Bengaluru. It is not case with Maysuru"
x = re.search("not",text)
y = re.search("^I",text)
z = re.search("uru$",text)   #r = re.search("ur$",text)
p = re.search("of..",text)
q = re.search("..uru",text)
r = re.findall(".*uru",text)
i = re.search("\AIt",text)
a = re.findall("..uru",text)
# print(x)
# print(y)
# print(z)
# print(p)
# print(q)
# print(r)
# print(i)
# print(a)

print(re.findall.__doc__)

""""iedjkwnkfjewjwifdsf=09kjb;vjknnnindklmd.f,mswklejfghbdm,slkoaijuhsgvd nbnmnjsdhufyvbnmdkjhhbdnmjhkdhggmfbdhbhjbnjh,mn"""