#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    # """ Approach 1: Recursion with Memoization O(N), O(N) """
    # def __init__(self):
    #     self.memo = {}

    # def rob(self, nums: List[int]) -> int:

    #     self.memo = {}

    #     return self.robFrom(0, nums)

    # def robFrom(self, i, nums):

    #     # No more houses left to examine.
    #     if i >= len(nums):
    #         return 0

    #     # Return cached value.
    #     if i in self.memo:
    #         return self.memo[i]

    #     # Recursive relation evaluation to get the optimal answer.
    #     ans = max(
    #         self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i]
    #     )

    #     # Cache for future use.
    #     self.memo[i] = ans
    #     return ans
    
    # """ Approach 2: Dynamic Programming O(N), O(N) """
    # def rob(self, nums: List[int]) -> int:

    #     # Special handling for empty case.
    #     if not nums:
    #         return 0

    #     maxRobbedAmount = [None for _ in range(len(nums) + 1)]
    #     N = len(nums)

    #     # Base case initialization.
    #     maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

    #     # DP table calculations.
    #     for i in range(N - 2, -1, -1):

    #         # Same as recursive solution.
    #         maxRobbedAmount[i] = max(
    #             maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i]
    #         )

    #     return maxRobbedAmount[0]
    
    """ Approach 3: Optimized Dynamic Programming O(N), O(1) """
    def rob(self, nums: List[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):

            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next

        
# @lc code=end

