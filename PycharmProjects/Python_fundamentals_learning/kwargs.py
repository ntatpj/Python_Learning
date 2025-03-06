def kw(**kwargs):
    print("the key is and value is", kwargs)
    # print("items are", kwargs.items())
    for key, value in kwargs.items():
    #     print(f"the key is {i} and the value is {j}")
        print(f"the key is %s,tha vlaue is %s" %(key,value))
        print("name = ",kwargs[key])

kw(first = 'Geeks',second = "for")