a = 12345
n = len(str(a))
#for i in range (n):
   #  i = i-1
   # #print(n)
   #  b = a%10
   #  print(b,end="")
   #  a = a//10
   #  #print(a)

reverse_number=0
while a != 0:
    b = a%10
    reverse_number=reverse_number*10 + b
    a = a//10
print(reverse_number)