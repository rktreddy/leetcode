#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     """ Approach 1: Linear Scan """
    #     first_num = float("inf")
    #     second_num = float("inf")
    #     for n in nums:
    #         if n <= first_num:
    #             first_num = n
    #         elif n <= second_num:
    #             second_num = n
    #         else:
    #             return True
    #     return False
    
    def increasingTriplet(self, nums: List[int]) -> bool:
        """ Practice: Approach 1: Linear Scan O(n), O(1) """
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False

# @lc code=end

