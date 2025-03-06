class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def NodetoLinkedList(list1):
    start_node = Node(list1[0])
    temp = start_node
    current_node = start_node
    # hashlist.append(current_node)
    # print(temp, temp.val, temp.next)
    for i in list1[1:]:
        current_node = Node(i)
        # hashlist.append(current_node)
        temp.next = current_node
        temp = current_node
        # print(temp, temp.val, temp.next)
    return start_node
#
def FindLinkedlistcomponent(head):
    counter = 0
    prelist = []
    temp = head
    current_node = temp.next
    while current_node is not None:
        # print(temp.val,current_node.val)
        if temp.val in nums and current_node.val in nums:
            # prelist = []
            prelist.append(temp.val)
            prelist.append(current_node.val)
            counter +=1
            # print("counter value is",counter)
        # elif current_node.next is None and current_node.val in list1:
        elif temp.val in nums and temp.val not in prelist:
            counter +=1
        temp = temp.next
        current_node = temp.next
    if temp.val in nums and temp.val not in prelist:
        counter += 1
    return counter








x=input("Enter list and keep space between two elements of list")
list1 = []
list1 = x.split(" ")
y = input("enter nums")
nums = []
nums = y.split(" ")
# print(nums)
start_node = NodetoLinkedList(list1)
# print(start_node)
print(FindLinkedlistcomponent(start_node))