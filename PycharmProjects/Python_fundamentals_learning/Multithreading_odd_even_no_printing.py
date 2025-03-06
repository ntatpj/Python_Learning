import threading

def printeven():
    for i in range(0,101,2):
        print(i)

def printodd():
    for i in range(1,100,2):
        print(i)

t1 = threading.Thread(target= printeven)
t2 = threading.Thread(target= printodd)

t1.start()
t2.start()

t1.join()
t2.join()

print("DOne")