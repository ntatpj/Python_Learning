class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.prev = None

def NodetoDoublyLinkedList_and_FindPalindrome(inputlist):
    list = inputlist
    # print(list)
    start_node = Node(list[0])
    current_node = start_node
    temp = start_node
    # print(temp.prev, temp.val, temp.next, temp)
    for i in list[1:]:
        # print(i)
        current_node = Node(i)
        temp.next = current_node
        current_node.prev = temp
        # print(temp.prev,temp.val,temp.next,"jdsk",temp)
        temp = temp.next
    # print(temp.prev, temp.val, temp.next, "jdsk", temp)
    temp.next = start_node
    start_node.prev = temp
    end_node = temp
    temp1 = start_node
    temp2 = end_node
    # print("start node is",start_node.prev, start_node.val, start_node.next, start_node)
    while temp1.val == temp2.val:
        temp1 = temp1.next
        temp2 = temp2.prev
        if temp1 == end_node and temp2 == start_node:
            return True
    return False







x=input("Enter list and keep space between two elements of list")
list = x.split(" ")
print(NodetoDoublyLinkedList_and_FindPalindrome(list))