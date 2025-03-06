from typing import Optional
# pos = 1
hashlist = []
# list = [3,2,0,-4]
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None


def NodetoLinkedList(list):
    # print(list)
    start_node = Node(list[0])
    # print(start_node.val)
    temp = start_node
    current_node = start_node
    hashlist.append(current_node)
    # print(temp, temp.val, temp.next)
    for i in list[1:]:
        current_node = Node(i)
        hashlist.append(current_node)
        temp.next = current_node
        temp = current_node
        # print(temp, temp.val, temp.next)
    print(hashlist)
#below line creates circular linkedlist at pos [1]
    temp.next = hashlist[pos]
    return start_node
    # print(temp.next,temp.val)

    # print(temp, temp.val, temp.next)
    # print(start_node.next)

#
def traverselist(start_node):
    trave = start_node
    while trave is not None:
        # print(trave, trave.val)
        trave = trave.next


#
def checkifcircular(start_node):
    temp = start_node
    # print("temp is", temp)
    lsty = []
    try:
        while temp not in lsty:
            # print("temp is",temp)
            lsty.append(temp)
            temp = temp.next
        return (lsty.index(temp))
    except:
        # print("lsyt is", lsty)
        return False


x=input("Enter list and keep space between two elements of list")
list = x.split(" ")
pos = int(input("ENter pos"))
start_node = NodetoLinkedList(list)
# traverselist(start_node)
print(checkifcircular(start_node))
print("global value of start is",start_node)
