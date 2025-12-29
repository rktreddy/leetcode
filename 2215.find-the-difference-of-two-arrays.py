#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """ Approach 1: Set O(n+m), O(n+m) """
        set1 = set(nums1)
        set2 = set(nums2)

        only_in_nums1 = list(set1 - set2)
        only_in_nums2 = list(set2 - set1)

        return [only_in_nums1, only_in_nums2]
    
        
# @lc code=end

