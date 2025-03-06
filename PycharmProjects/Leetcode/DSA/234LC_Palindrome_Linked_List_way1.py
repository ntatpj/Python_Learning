class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
hashlist = []

def NodetoLinkedList(list):
    start_node = Node(list[0])
    temp = start_node
    current_node = start_node
    hashlist.append(current_node.val)
    # print(temp, temp.val, temp.next)
    for i in list[1:]:
        current_node = Node(i)
        hashlist.append(current_node.val)
        temp.next = current_node
        temp = current_node
        # print(temp, temp.val, temp.next)
    # return hashlist[::-1]
    if hashlist == hashlist[::-1]:
        return True
    else:
        return False























x=input("Enter list and keep space between two elements of list")
list = x.split(" ")
print(NodetoLinkedList(list))