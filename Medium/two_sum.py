class Solution:
    def twoSum(self, nums: list[int],target: int) -> list[int]:
        prev_element_list = {}  #dictornary holding vlaue as key and index as value

        for inx,value in enumerate(nums):
            other_num = target - value
            if other_num in prev_element_list:
                return(prev_element_list[other_num],inx)
            prev_element_list[value]= inx
            # print(prev_element_list)

obj = Solution()
print(obj.twoSum([2,7,11,15],9))
#comment
#server_var_keleli_comment 2
