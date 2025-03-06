# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    start_node = None

    def mergeTwoLists(list1, list2):
        new_list = None
        global start_node
        while True:
            # print("its while loop")
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
                        # print(list1.val, list2.val)
                else:  # if list2 is None
                    if new_list is None:
                        new_list = list1
                        start_node = new_list
                    else:
                        new_list.next = list1
                    break
            else:  # if list1 is None
                if list2 is not None:
                    if new_list is None:
                        new_list = list2
                        start_node = new_list
                    else:
                        new_list.next = list2
                break

            list1 = start_node  # this is because we are putting list1 as argument in mergeklists
            # print(f"tridev,",start_node.val,"ooo",new_list.val,"ooo",list1)
            return start_node

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        else:
            l1 = lists[0]
            for i in range(1, len(lists)):
                # print("YOyo", list1.val, start_node.val)
                # traverselist(list1)
                l1 = Solution.mergeTwoLists(l1, lists[i])
                # print(l1,l1,start_node)
            # return start_node
            result = Solution.traverselist(start_node)
            return result

    def traverselist(head):
        revlist = []
        trave = head
        while trave is not None:
            revlist.append(trave)
            trave = trave.next
        return revlist


