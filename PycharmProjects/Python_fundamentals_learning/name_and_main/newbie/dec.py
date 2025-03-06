# Enter your code here. Read input from STDIN. Print output to STDOUT

n_m = input()  # n &m intergers
N_M = []
jojo = n_m.split()
n_mset = list(map(int, jojo))
for i in range(0, len(n_mset)):
    if i in range(1,((n_mset[i] <= pow(10, 5)))):
        N_M.append(n_mset[i])
    N = N_M[0]
    M = N_M[1]

    arr_inp = input()  # "n" no of elements in Array given by user
    ARRAY = []  # defined empty array list

    Am = input()  # elements in set A
    A_ARRAY = []  # defined A cha final Array

    Bm = input()  # elements in set B
    B_ARRAY = []  # defined B cha final Arrya

    Arrs = arr_inp.split()  # converted input to list
    Arrayl = list(map(int, Arrs))  # converted list entties to integer
    for i in range(0, N):
        if ((1 <= Arrayl[i]) and (Arrayl[i] <= pow(10, 9))):
            ARRAY.append(Arrayl[i])
    Arrayu = set(ARRAY)  # converted let to set

    As = Am.split()
    Al = list(map(int, As))
    for i in range(0, M):
        if ((1 <= Al[i]) and (Al[i] <= pow(10, 9))):
            A_ARRAY.append(Al[i])
    A = set(A_ARRAY)

    Bs = Bm.split()
    Bl = list(map(int, Bs))
    for i in range(0, M):
        if ((1 <= Bl[i]) and (Bl[i] <= pow(10, 9))):
            B_ARRAY.append(Bl[i])
    B = set(B_ARRAY)

    Happiness = 0
    A_diff = A.difference(B)
    B_diff = B.difference(A)
    A_diff_sort = list(map(int, A_diff))
    A_diff_sort.sort()
    B_diff_sort = list(map(int, B_diff))
    B_diff_sort.sort()
    if (A_diff_sort == B_diff_sort):
        Aans = A.intersection(Arrayu)
    Ak = len(Aans)
    for i in range(0, Ak):
        Happiness += 1

    Bans = B.intersection(Arrayu)
    Bk = len(Bans)
    for I in range(0, Bk):
        Happiness -= 1

    print(Happiness)
