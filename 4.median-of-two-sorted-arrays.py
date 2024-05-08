#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxleftA = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
            minrightA = nums1[partitionA] if partitionA < m else float("inf")
            maxleftB = nums2[partitionB - 1] if partitionB > 0 else float("-inf")
            minrightB = nums2[partitionB] if partitionB < n else float("inf")

            if maxleftA <= minrightB and maxleftB <= minrightA:
                if (m + n) % 2 == 0:
                    return (max(maxleftA, maxleftB) + min(minrightA, minrightB)) / 2
                else:
                    return max(maxleftA, maxleftB)
            elif maxleftA > minrightB:
                right = partitionA - 1
            else:
                left = partitionA + 1           
        
# @lc code=end

