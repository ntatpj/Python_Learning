def swap_case(s):
    statement = input()
    for i in statement:
        result = ""
        match i:
            case(i.islower()):
                result += i.upper()
            case(i.isupper()):
                result += i.lower()
            case default:
                result += i
        return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


    # if i.islower():
    #     print(i.upper(),end="")
    # if i.isupper():
    #     print(i.lower(),end="")