def missing_pos_int(A):
    B=[]
    for x in A:
        if x > 0:
            B.append(x)
    B=set(B)
    B=list(B)
    B.sort()
    small_no=1
    for i in B:
        if i <= small_no:
            small_no +=1

        return(small_no)
    # print(B)




A=[-1,3,6,4,2,5,6,8]
print(missing_pos_int(A))