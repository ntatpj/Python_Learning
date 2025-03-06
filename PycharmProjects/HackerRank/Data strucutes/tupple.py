import builtins
n = int(input())
list = map(int, input().split())
tup = tuple(list)
print(hash(tup))