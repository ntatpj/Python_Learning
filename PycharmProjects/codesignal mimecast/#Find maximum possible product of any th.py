#Find maximum possible product of any three number in an array
def max_pos_product(A):
    A.sort()
    print(A)
    return max(A[0]*A[1]*A[-1],A[-1]*A[-2]*A[-3])
    # B=[]
    # for i in A:
    #     if i>0:
    #         B.append[i]
    # B=B.sort()
    # B=set(B)







A=[-60,-10,-30,1,2,-2,5,6]
print(max_pos_product(A))