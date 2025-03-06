# def pyfunc(r):
#
#     for x in range(r):
#
#         print(' '*(r-x-1)+'*'*(2*x+1))
#
# pyfunc(9)













#
# def print_triangle(n):
#     i = 0
#     for r in range(1,n+1):
#         print(' '*(n-r)+'*'*(r+i))
#         i += 1
#
# print_triangle(5)


def print_inverse_traingle(n):
    i = 0
    for r in range(0,n):
        print(' '*i +'*'*(2*n-1) )
        i +=1
        n -=1

print_inverse_traingle(65)
