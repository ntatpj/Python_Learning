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

def oddEvenList(start_node):
    tmp = start_node
    odd_node = start_node
    even_node_start = start_node.next
    even_node_temp = even_node_start
    while tmp:
        if tmp.next is None:
            odd_node.next = even_node_start
            even_node_temp.next = None
            # print(tmp.val)
            break
        tmp = tmp.next
        if tmp.next is None:
            odd_node.next = even_node_start
            even_node_temp.next =None
            # print(tmp.val)
            break
        odd_node.next=tmp.next
        odd_node=tmp.next
        tmp = tmp.next
        if tmp.next is None:
            odd_node.next = even_node_start
            even_node_temp.next = None
            # print(odd_node.val,odd_node.next.val,start_node.val,start_node.next.val)
            # print(tmp.val,tmp.next.val)
            break
        even_node_temp.next = tmp.next
        even_node_temp = tmp.next



def traverselist(head):
    # print(head.val)
    revlist = []
    trave = head
    # print(trave.next.val,)
    while trave is not None:
        # print(trave.val)
        revlist.append(int(trave.val))
        trave = trave.next
    print("revisedlistis",revlist)

x=input("Enter list and keep space between two elements of list")
list = x.split(" ")
start_node = NodetoLinkedList(list)
oddEvenList(start_node)
traverselist(start_node)