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


def reverseBetween(head, left:str,right:str):
    current_node = head
    # print("kkkk",current_node,current_node.val)
    temp = current_node
    left_node = None
    right_node = None
    # print(type(left),right)
    while temp is not None:
        # print(temp,temp.val)
        if temp.val == str(left):
            left_node = temp
        elif temp.val == str(right):
            right_node = temp
            right_node_copy =right_node
        temp = temp.next
    # print("left",left_node)
    # print("right", right_node)

    temp = current_node
    # print("ooooooooo",current_node,current_node.val)
    while temp is not None:
        temp = temp.next
        print(current_node.val)
        if temp == left_node:
            current_node.next = right_node
            right_node.next = temp
        elif temp == right_node_copy:
            current_node.next = left_node
            left_node.next = temp
        #     current_node = left_node
        current_node = temp
        # print(temp)

def traverselist(head):
    revlist = []
    trave = head
    while trave is not None:
        revlist.append(trave.val)
        trave = trave.next
    print("nex list is",revlist)


x=input("Enter list and keep space between two elements of list")
list = x.split(" ")
start_node = NodetoLinkedList(list)
# print(start_node.val)
reverseBetween(start_node,2,4)
# print(rev_start_node)
traverselist(start_node)




