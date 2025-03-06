class Solution:
    def list_to_linked_list(lst):
        if not lst:
            return None

        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            node = ListNode(val)
            current.next = node
            current = node

        return head

obj = Solution()
head = list_to_linked_list([3,2,0,-4])
print(obj.hasCycle(head))