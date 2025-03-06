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

def ReverseList(start_node):
    current_node =start_node
    prev_node = start_node
    next_node = start_node.next

    while next_node is not None:
        current_node = next_node
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
    start_node.next = None
    return current_node

def traverselist(head):
    revlist = []
    trave = head
    while trave is not None:
        revlist.append(trave.val)
        trave = trave.next
    print(revlist)

x=input("Enter list and keep space between two elements of list")
list = x.split(" ")
start_node = NodetoLinkedList(list)
# print(start_node.val)
rev_start_node = ReverseList(start_node)
# print(rev_start_node)
traverselist(rev_start_node)
