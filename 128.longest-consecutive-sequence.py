#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     """ Approach 1: Brute Force O(n^3), O(1) """
    #     longest_streak = 0

    #     for num in nums:
    #         current_num = num
    #         current_streak = 1

    #         while current_num + 1 in nums:
    #             current_num += 1
    #             current_streak += 1

    #         longest_streak = max(longest_streak, current_streak)

    #     return longest_streak
    
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     """ Approach 2: Sorting O(n logn), o(logn) or o(n)"""
    #     if not nums:
    #         return 0

    #     nums.sort()

    #     longest_streak = 1
    #     current_streak = 1

    #     for i in range(1, len(nums)):
    #         if nums[i] != nums[i - 1]:
    #             if nums[i] == nums[i - 1] + 1:
    #                 current_streak += 1
    #             else:
    #                 longest_streak = max(longest_streak, current_streak)
    #                 current_streak = 1

    #     return max(longest_streak, current_streak)

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     """ Approach 3: HashSet and Intelligent Sequence Building O(n), O(n)"""
    #     longest_streak = 0
    #     num_set = set(nums)

    #     for num in num_set:
    #         if num - 1 not in num_set:
    #             current_num = num
    #             current_streak = 1

    #             while current_num + 1 in num_set:
    #                 current_num += 1
    #                 current_streak += 1

    #             longest_streak = max(longest_streak, current_streak)

    #     return longest_streak
    
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     """ Hash Set O(n), O(n) """
    #     numSet = set(nums)
    #     longest = 0

    #     for n in numSet:
    #         # check if its the start of a sequence
    #         if (n - 1) not in numSet:
    #             length = 1
    #             while (n + length) in numSet:
    #                 length += 1
    #             longest = max(length, longest)
    #     return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        """ Hash Set O(n), O(n) """
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

        
# @lc code=end

