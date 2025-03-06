if __name__ == '__main__':
    s = input()
    if 0 < len(s) <1000:
        isalphanumeric = False
        isalpha = False
        isnumeric = False
        islower = False
        isupper = False
        list1 = list(map(str,s))
        # print(list1)
        for i in s:
            if i.isalpha():
                isalpha = True
                if i.islower():
                    islower = True
                elif i.isupper():
                    isupper = True
            if i.isnumeric():
                isnumeric = True
            if isalpha or isnumeric:
                isalphanumeric = True

        print(isalphanumeric)
        print(isalpha)
        print(isnumeric)
        print(islower)
        print(isupper)


