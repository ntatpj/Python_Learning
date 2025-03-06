def count_substring(string, sub_string):
    if 1<= len(string)<=200:
        length_of_substring = len(sub_string)
        j = 0
        for i in range (0, (len(string)-len(sub_string)+1)):
            if string[i] == sub_string[0] and string[i:i+length_of_substring]==sub_string:
                # print(string[i:i+length_of_substring])
                j += 1
        return(j)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

#0/1/2/3/4
3
4