def fuct(A):
    seen=set()
    L=0
    count=0

    for R in range (len(A)):
        while A[R] in seen:
            seen.remove(A[L])
            L +=1
        seen.add(A[R])
        count+=(R-L+1)
    return count

A = [3,4,5,5,2]

print(fuct(A))
