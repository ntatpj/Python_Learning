class Solution:
    def myAtoi(self, s):
        if 0 <= len(s) <= 200:
            for i in s:
                try:
                    if i == "-" or i == "+" or 0 <= int(i) <= 99 :
                        print (i,end="")
                except ValueError:
                    continue



object = Solution()
s = input("Enter the string:")
object.myAtoi(s)


