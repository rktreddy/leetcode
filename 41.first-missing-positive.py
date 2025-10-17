#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     """ Approach 1: Boolean Array O(n), O(n) """
    #     n = len(nums)
    #     seen = [False] * (n + 1)  # Array for lookup

    #     # Mark the elements from nums in the lookup array
    #     for num in nums:
    #         if 0 < num <= n:
    #             seen[num] = True

    #     # Iterate through integers 1 to n
    #     # return smallest missing positive integer
    #     for i in range(1, n + 1):
    #         if not seen[i]:
    #             return i

    #     # If seen contains all elements 1 to n
    #     # the smallest missing positive number is n + 1
    #     return n + 1
    

    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     """ Approach 2: Index as a Hash Key O(n), O(n): auxiliary space O(1) """
    #     n = len(nums)
    #     contains_1 = False

    #     # Replace negative numbers, zeros,
    #     # and numbers larger than n with 1s.
    #     # After this nums contains only positive numbers.
    #     for i in range(n):
    #         # Check whether 1 is in the original array
    #         if nums[i] == 1:
    #             contains_1 = True
    #         if nums[i] <= 0 or nums[i] > n:
    #             nums[i] = 1

    #     if not contains_1:
    #         return 1

    #     # Mark whether integers 1 to n are in nums
    #     # Use index as a hash key and negative sign as a presence detector.
    #     for i in range(n):
    #         value = abs(nums[i])
    #         # If you meet number a in the array - change the sign of a-th element.
    #         # Be careful with duplicates : do it only once.
    #         if value == n:
    #             nums[0] = -abs(nums[0])
    #         else:
    #             nums[value] = -abs(nums[value])

    #     # First positive in nums is smallest missing positive integer
    #     for i in range(1, n):
    #         if nums[i] > 0:
    #             return i

    #     # nums[0] stores whether n is in nums
    #     if nums[0] > 0:
    #         return n

    #     # If nums contained all elements 1 to n
    #     # the smallest missing positive number is n + 1
    #     return n + 1
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ Approach 3: Cycle Sort O(n), O(n): auxiliary space O(1) """

        n = len(nums)

        # Use cycle sort to place positive elements smaller than n
        # at the correct index
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                # swap
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # Iterate through nums
        # return smallest missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all elements are at the correct index
        # the smallest missing positive number is n + 1
        return n + 1
        
# @lc code=end

