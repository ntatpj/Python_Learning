class Node:
    def __init__(self,x):
        self.val = x
        self.next = None


x = int(input())
if x is 0:
    return None
newlist = Node(x)
start_node = newlist

while x != 0:
    x=int(input())
    temp = Node(x)
    newlist.next = temp
    newlist = newlist.next



def traverselist(head):
    revlist = []
    trave = head
    while trave is not None:
        revlist.append(trave.val)
        trave = trave.next
    print("nex list is",revlist)

traverselist(start_node)