#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     """ Approach 1: Two Pointers T:O(n^2), S:O(logn) to O(n)"""
    #     diff = float("inf")
    #     nums.sort()
    #     for i in range(len(nums)):
    #         lo, hi = i + 1, len(nums) - 1
    #         while lo < hi:
    #             sum = nums[i] + nums[lo] + nums[hi]
    #             if abs(target - sum) < abs(diff):
    #                 diff = target - sum
    #             if sum < target:
    #                 lo += 1
    #             else:
    #                 hi -= 1
    #         if diff == 0:
    #             break
    #     return target - diff
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """ Approach 2: Binary Search T: O(n^2 log n), S: O(log n) to O(n) """
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
        
# @lc code=end

