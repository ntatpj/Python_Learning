class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

new_list = None
start_node = None
def mergeTwoLists(list1, list2):
    global new_list
    global start_node
    while True:
        # print("list1val is",list1.val)
        # print("list2 val is",list2.val)
        if list1 is not None:
            if list2 is not None:
                if list1.val < list2.val:
                    if new_list is None:
                        new_list = ListNode(list1.val)
                        start_node = new_list
                    else:
                        new_list.next = ListNode(list1.val)
                        new_list = new_list.next
                    list1 = list1.next
                elif list2.val < list1.val:
                    if new_list is None:
                        new_list = ListNode(list2.val)
                        start_node = new_list
                    else:
                        new_list.next = ListNode(list2.val)
                        new_list = new_list.next
                    list2 = list2.next
                elif list1.val == list2.val:
                    if new_list is None:
                        new_list = ListNode(list1.val)
                        start_node = new_list
                        new_list.next = ListNode(list2.val)
                        new_list = new_list.next
                    else:
                        new_list.next = ListNode(list1.val)
                        new_list = new_list.next
                        new_list.next = ListNode(list2.val)
                        new_list = new_list.next
                    list1 = list1.next
                    list2 = list2.next
                    print(list1.val,list2.val)
            else:
                if new_list is None:
                    new_list = list1
                    start_node = new_list
                else:
                    new_list.next = list1
                break
        else:
            if list2 is not None:
                if new_list is None:
                    new_list = list2
                    start_node = new_list
                else:
                    new_list.next = list2
            break
    # print(start_node)
    return start_node





def NodetoLinkedList(list):
    start_node = ListNode(list[0])
    temp = start_node
    current_node = start_node
    # hashlist.append(current_node)
    # print(temp, temp.val, temp.next)
    for i in list[1:]:
        current_node = ListNode(i)
        # hashlist.append(current_node)
        temp.next = current_node
        temp = current_node
        # print(temp, temp.val, temp.next)
    return start_node



def traverselist(head):
    revlist = []
    trave = head
    while trave is not None:
        revlist.append(trave.val)
        trave = trave.next

    print("nex list is",revlist)


x=input("Enter list and keep space between two elements of list")
listy1 = x.split(" ")
listy1 = [int(float(j)) for j in listy1]
print(listy1)
num1 = NodetoLinkedList(listy1)
# num1=None
h=input("Enter list and keep space between two elements of list")
listy2 = h.split(" ")
listy2 = [int(float(u)) for u in listy2]
print(listy2)
num2 = NodetoLinkedList(listy2)


l = mergeTwoLists(num1, num2)
# traverselist(nums1)
# traverselist(nums2)

traverselist(l)