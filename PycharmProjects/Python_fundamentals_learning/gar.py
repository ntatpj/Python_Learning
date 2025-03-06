from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Createlinkedlistandcircularll:



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False

# obj = Solution
# list_node_obj = ListNode([3,2,0,-4])
# print(obj.hasCycle(list_node_obj))

obj = Solution()
head = ListNode([3,2,0,-4])
print(obj.hasCycle(head))
print(obj)