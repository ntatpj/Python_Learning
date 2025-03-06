class Node:
    def __init__(self,x):
        self.val = x
        self.next = None


def NodetoLinkedList(list):
    start_node = Node(list[0])
    temp = start_node
    current_node = start_node
    # hashlist.append(current_node)
    # print(temp, temp.val, temp.next)
    for i in list[1:]:
        current_node = Node(i)
        # hashlist.append(current_node)
        temp.next = current_node
        temp = current_node
        # print(temp, temp.val, temp.next)
    return start_node



def addTwoNumbers(l1, l2):
    sum = Node()





x=input("Enter list and keep space between two elements of list")
list = x.split(" ")
start_node = NodetoLinkedList(list)
# print(start_node.val)
addTwoNumbers(start_node,2,4)
# print(rev_start_node)
# traverselist(start_node)
