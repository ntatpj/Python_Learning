def inc(x):
    return x +1

def operate(funct,x):
    result = funct(x)
    return result

print(operate(inc, 3))