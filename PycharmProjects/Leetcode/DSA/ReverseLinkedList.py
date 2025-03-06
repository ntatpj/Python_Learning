from typing import Optional


class ListNode:
    def __init__(self, val=0, neqt=None):
        self.val = val
        self.neqt = neqt


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head
        start_node = None
        temp = None

        for i in head:
            # print(i)
            current_node = ListNode(i)
            if start_node is None:
                start_node = current_node
            else:
                temp.neqt = current_node
            temp = current_node
        # print(start_node.val)
        carnod = start_node
        while carnod.neqt is not None:
            print(carnod.val)
            print(carnod.neqt)
            carnod = carnod.neqt
        print(carnod.val)
        print(carnod.neqt)

        # present_node = None
        # current_node = None
        # next_node = None

        # while i in range (len(self.head)-3):
        #     present_node = start_node
        #     carrent_node = present_node.neqt
        #     next_node = carrent_node.neqt

    




okj = Solution()
okj.reverseList([1,2,3,4,5])