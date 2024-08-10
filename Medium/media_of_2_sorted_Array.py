class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        listfinal =[]
        listfinal = nums1+nums2
        listfinal.sort()
        print(listfinal)
        m = (len(listfinal))
        n = m-1
        print(n)
        rem = (m%2)
        if rem ==0:
            print(listfinal[int((n + 1) / 2)])
            print(listfinal[int(n / 2)])
            med_even = (listfinal[int((n + 1) / 2)] + listfinal[int(n / 2)])/2
            print("Median of even is:", med_even)
        else:
            med_odd = listfinal[int(((n + 1) / 2))]
            print("Median of odd is:", med_odd)
        #
        # if x%2 == 0:
        #     print(x+1)
        # # else:
        #     print(((listfinal((x + 1) / 2)+ listfinal(x / 2))/2))




obj = Solution()
obj.findMedianSortedArrays([324,2,1,3],[3,34,9])