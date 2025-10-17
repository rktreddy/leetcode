#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     """ Approach 1: Dynamic Programming O(N^2), O(N) """
    #     dp = [1] * len(nums)
    #     for i in range(1, len(nums)):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)
    
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     """ Approach 2: Intelligently Build a Subsequence O(N^2), O(N) """
    #     sub = [nums[0]]

    #     for num in nums[1:]:
    #         if num > sub[-1]:
    #             sub.append(num)
    #         else:
    #             i = 0
    #             while num > sub[i]:
    #                 i += 1
    #             sub[i] = num
    #     return len(sub)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ Approach 3: Improve With Binary Search O(N log N), O(N) """
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)

        
# @lc code=end

