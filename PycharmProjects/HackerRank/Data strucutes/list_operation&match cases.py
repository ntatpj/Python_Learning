# if __name__ == '__main__':
#     N = int(input())
#     list = []
#     for x in range(N +2):
#         i, *e = input().split()
#         # print(f"I just inputed {i} and {e}")
#         if i == "insert":
#             list.insert(int(e[0]),int(e[1]))
#             # print(list)
#         if i == "print":
#             print(list)
#         if i == "remove":
#             list.remove(int(e[0]))
#         if i == "append":
#             list.append(int(e[0]))
#         if i == "sort":
#             list.sort()
#         if i == "pop":
#             list.pop()
#         if i == "reverse":
#             list.reverse()
#     # print(list)




if __name__ == '__main__':
    N = int(input())
    list = []
    for x in range(N +2):
        i, *e = input().split()
        # print(f"I just inputed {i} and {e}")
        match i:
            case "insert":
                list.insert(int(e[0]),int(e[1]))
            # print(list)
            case "print":
                print(list)
            case "remove":
                list.remove(int(e[0]))
            case "append":
                list.append(int(e[0]))
            case "sort":
                list.sort()
            case "pop":
                list.pop()
            case "reverse":
                list.reverse()
    # print(list)
