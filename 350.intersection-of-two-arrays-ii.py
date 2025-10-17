#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ hashmap """

        count = {}
        res = [] 

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res 
    

    
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """ hashmap with Counter"""

    #     count = Counter(nums1)
    #     res = [] 

    #     for num in nums1:
    #         count[num] = count.get(num, 0) + 1

    #     for num in nums2:
    #         if num in count and count[num] > 0:
    #             res.append(num)
    #             count[num] -= 1
    #     return res 
        
# @lc code=end

