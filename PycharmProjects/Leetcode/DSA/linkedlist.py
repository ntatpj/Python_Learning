import self as self

# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None
#
#
# class Linkedlist:
#     def __init__(self):
#         self.start_node = None
#         self.temp = None
#
#     def newnodeinsert(self,value):
#         new_node = Node(value)
#         while new_node.data !=0:
#             if self.start_node is None:
#                 start_node = new_node
#                 temp = new_node
#             else:
#                 temp.next = new_node
#
#             temp = new_node

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

start_node = None
temp = None

while True:
    var = int(input("Enter the data to be stored in Linkedlist and enter 0 when done"))
    if var == 0:
        break
    else:
        node_obj = Node(var)
        if start_node is None:
            start_node = node_obj
            temp = node_obj
        else:
            temp.next = node_obj
            print("conti temp.next is",temp.next)
            temp = node_obj
            print("conti current temp data is",temp.data)


if start_node is not None:
    temp = start_node
    while temp is not None:
        print(temp.data)
        temp = temp.next
    # print("addr of start node is", temp.next)
    # while True:
    #     # print("addr of temp is",temp.next)
    #     print(temp.data)
    #     temp = temp.next
    #     # print("temp.next is",temp.next)
    #     if temp.next is None:
    #         print(temp.data)
    #         break




