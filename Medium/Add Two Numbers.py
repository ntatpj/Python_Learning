class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        diff = len(l1) - len(l2)
        while diff != 0:
            if len(l1)>len(l2):
                l2.append(0)
            elif len(l1)<len(l2):
                l1.append(0)
            diff -=1
        print(l1,l2)









obj = Solution
obj.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])








# diff =3
# l = [2,12,312,4]
# while diff !=0:
#     l.append(0)
#     diff -=1
# print(l)