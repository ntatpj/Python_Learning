def swap_case(s):
    sent = ""
    if 0 < len(s) <= 1000:
        for i in s:
            if i.islower():
                sent = sent+ (i.upper())
            elif i.isupper():
                sent = sent+(i.lower())
            else:
                sent = sent + i
        return sent


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)




