#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    # def longestOnes(self, nums: List[int], k: int) -> int:
    #     """ Approach: Sliding Window O(N), O(1)"""
    #     left = 0
    #     for right in range(len(nums)):
    #         k -= 1 - nums[right]

    #         if k < 0:
    #             k += 1 - nums[left]
    #             left += 1
    #     return right - left + 1
    
    # def longestOnes(self, nums: List[int], k: int) -> int:
    #     """ practice: Approach: Sliding Window O(N), O(1) """
    #     left = 0
    #     for right in range(len(nums)):
    #         k -= 1 - nums[right]

    #         if k < 0:
    #             k += 1 - nums[left]
    #             left += 1
    #         print(f'left: {left}, right: {right}, num: {nums[right]}, k: {k}')
                  
    #     return right - left + 1

    def longestOnes(self, nums: List[int], k: int) -> int:
        """ practice: Approach: Sliding Window O(N), O(1) """
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1

# @lc code=end
# left = 0; k = 2
# right = 0; num = 1; k = 2
# right = 1; num = 1; k = 2
# right = 2; num = 1; k = 2
# right = 3; num = 0; k = 1
# right = 4; num = 0; k = 0
# right = 5; num = 0; k = -1
# right = 5; num = 0; left = 0; k = 0
# right = 6; num = 1; k = 0
# right = 7; num = 1; k = 0
# right = 8; num = 1; k = 0
# right = 9; num = 1; k = 0
# right = 10; num = 0; k = -1
# right = 10; num = 0; left = 2; k = 0

# 10 - 2 + 1 = 9






