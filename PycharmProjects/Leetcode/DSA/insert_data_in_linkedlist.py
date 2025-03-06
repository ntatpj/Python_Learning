from typing import Optional


class ListNode:
    def __init__(self, val=0, neqt=None):
        self.val = val
        self.neqt = neqt


class Solution:
    def __init__(self):
        self.head_list = None
        self.start_node = None
    def makelist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head_list = head
        self.start_node = None
        temp = None

        for i in self.head_list:
            # print(i)
            current_node = ListNode(i)
            if self.start_node is None:
                self.start_node = current_node
            else:
                temp.neqt = current_node
            temp = current_node
        # print(start_node.val)
        carnod = self.start_node
        while carnod.neqt is not None:
            print(carnod.val)
            carnod = carnod.neqt
        print(carnod.val)

    def insertinlist(self, num_to_insert:int, after_exsisting_num:int):
        if num_to_insert not in self.head_list and after_exsisting_num in self.head_list:
            temp = self.start_node
            while temp.val != after_exsisting_num:
                temp = temp.neqt
            inserted_node = ListNode(num_to_insert)
            var = temp.neqt
            temp.neqt = inserted_node
            inserted_node.neqt = var
        carnod = self.start_node
        while carnod.neqt is not None:
            print("modified",carnod.val)
            carnod = carnod.neqt
        print("modified",carnod.val)


okj = Solution()
okj.makelist([1, 2, 3, 4, 5,6])
okj.insertinlist(8,4)