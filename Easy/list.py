class Solution:
    def threeSum(self, nums):
        while 3 <= len(nums) <= 3000:
            triplet = []
            sorted_triplet = []
            for i in range(len(nums)-1):
                j = i+1
                k_th_var = 0 - nums[i]-nums[j]
                if k_th_var in nums:
                    k=nums.index(k_th_var)
                    triplet.append(sorted([nums[i],nums[j],nums[k]]))
                    sorted_triplet = triplet
            for i in range(len(sorted_triplet)-1):
                try:
                    if sorted_triplet[i]==sorted_triplet[i+1]:
                        sorted_triplet.remove(sorted_triplet[i+1])
                    return (sorted_triplet)
                except:
                    continue


obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))