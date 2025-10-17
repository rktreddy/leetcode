#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     """ Approach 1: Linear Scan O(n), O(1) """
    #     i = 0
    #     while arr[i] < arr[i + 1]:
    #         i += 1
    #     return i 
    
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """ Approach 2: Binary Search O(log2 n), O(1) """
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l 


        
# @lc code=end

