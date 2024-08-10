a = int(input("Enter the number"))
def fibonaci(a):
    if a == 0:
        print(0)
    elif a ==1:
        print(1)
    else:
        result = 0
        first_num =0
        second_num=1
        first_num = second_num
        second_num = result
        result = first_num + second_num
        print(result)

for i in range(a+1):
    fibonaci(a)


