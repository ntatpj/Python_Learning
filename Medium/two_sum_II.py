class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        j = len(nums) - 1
        i = 0
        while i<j:
            curSum = nums[i] + nums[j]
            if curSum > target:
                j -= 1
            elif curSum < target:
                i += 1
            else:
                return[i+1,j+1]
        # for k in range(0,len(nums)):
        #     i = k
        #     print("i is",i)
        #     print("j is",j)

obj = Solution()
print(obj.twoSum([1,2,3,4],6))