def greet(x):
    def say():
        print("Hello, Welcome")
        print("Thanks for using me!")
        x()
    return say()

# @greet
def printit():
    print("What is your name?")



# neha = greet(printit)
# neha()
greet(printit)
# printit()