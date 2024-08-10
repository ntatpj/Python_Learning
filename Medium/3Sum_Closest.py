from itertools import combinations,permutations
class Solution:
    def threeSumClosest(self, nums,target):
        diff = float('inf')
        nums.sort()
        for i, num in enumerate(nums):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = num + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum

                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break

        return target - diff

obj = Solution()
print(obj.threeSumClosest([-1,2,1,-4],1))