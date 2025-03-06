#this program will help you find is the given IP address is valid or not

import re
text = "255.255.688.ff9"
if len(text) > 15:
    print("Not a valid IP address")    #not more than 15 so not valid IP address
else:
    #list = []
    print(text)
    list=re.split('\.',text)
    print(list)
    for i in range(0,4):
        if int(list[i]) <= 255:
            IPval = True
        else:
            IPval = False
            break
    if IPval:
        print("Is a valid IP address")
    else:
        print("s not a valid IP address")



