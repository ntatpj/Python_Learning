print(x>3)
import math
try:
    math.sqrt(-10)
except ValueError:
    print("kuch naya try karo")
else:
    sum = 10
    print(sum)
finally:
    print("OK! I belong to finally")

