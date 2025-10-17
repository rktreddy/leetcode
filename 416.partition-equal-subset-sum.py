#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    # def canPartition(self, nums: List[int]) -> bool:
    #     """ Approach 1: Brute Force O(2^n, O(N))"""
    #     def dfs(nums: List[int], n: int, subset_sum: int) -> bool:
    #         # Base cases
    #         if subset_sum == 0:
    #             return True
    #         if n == 0 or subset_sum < 0:
    #             return False
            
    #         result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
    #                   or dfs(nums, n - 1, subset_sum))
    #         return result
        
    #     total_sum = sum(nums)

    #     if total_sum % 2 != 0:
    #         return False
        
    #     subset_sum = total_sum // 2
    #     n = len(nums)
    #     return dfs(nums, n - 1, subset_sum)
    
    # def canPartition(self, nums: List[int]) -> bool:
    #     """ Approach 2: Top Down Dynamic Programming - Memoization O(m n), O(m n)""" 

    #     @lru_cache(maxsize=None)
    #     def dfs(nums: Tuple[int], n: int, subset_sum: int) -> bool:
    #         # Base cases
    #         if subset_sum == 0:
    #             return True
    #         if n == 0 or subset_sum < 0:
    #             return False
    #         result = (dfs(nums, n - 1, subset_sum - nums[n - 1])
    #                 or dfs(nums, n - 1, subset_sum))
    #         return result

    #     # find sum of array elements
    #     total_sum = sum(nums)

    #     # if total_sum is odd, it cannot be partitioned into equal sum subsets
    #     if total_sum % 2 != 0:
    #         return False

    #     subset_sum = total_sum // 2
    #     n = len(nums)
    #     return dfs(tuple(nums), n - 1, subset_sum)

    
    # def canPartition(self, nums: List[int]) -> bool:
    #     """ Approach 3: Bottom Up Dynamic Programming O(m n), O(m n) """
    #     # find sum of array elements
    #     total_sum = sum(nums)

    #     # if total_sum is odd, it cannot be partitioned into equal sum subsets
    #     if total_sum % 2 != 0:
    #         return False
    #     subset_sum = total_sum // 2
    #     n = len(nums)

    #     # construct a dp table of size (n+1) x (subset_sum + 1)
    #     dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
    #     dp[0][0] = True
    #     for i in range(1, n + 1):
    #         curr = nums[i - 1]
    #         for j in range(subset_sum + 1):
    #             if j < curr:
    #                 dp[i][j] = dp[i - 1][j]
    #             else:
    #                 dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
    #     return dp[n][subset_sum]

    
    def canPartition(self, nums: List[int]) -> bool:
        """ Approach 4: Optimised Dynamic Programming - Using 1D Array O(m n), o(m) """
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2

        dp = [False] * (subset_sum + 1)
        dp[0] = True

        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]
        
# @lc code=end

