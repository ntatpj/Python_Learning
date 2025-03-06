# s = "1ASsfdjfkffjkkdfkjdnf"
# o = (s[0:3])
# print(o)

import textwrap
#
# def wrap(string, max_width):
#     if 0 < len(string) < 1000 and 0 < max_width < len(string):
#         for i in range(0,len(string),max_width):
#             print (string[i:i+max_width])
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     # print(result)



import textwrap

def wrap(string, max_width):
    if 0 < len(string) < 1000 and 0 < max_width < len(string):
        wrapper = textwrap.TextWrapper(width=4)
        word_list = wrapper.wrap(text=string)
        return (word_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)