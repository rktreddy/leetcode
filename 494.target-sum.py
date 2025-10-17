#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     """ most voted """
    #     dic = defaultdict(int)

    #     def dfs(index = 0, total = 0):
    #         key = (index, total)

    #         if key not in dic:
    #             if index == len(nums):
    #                 if index == len(nums):
    #                     return 1 if total == target else 0
    #                 else:
    #                     dic[key] = dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])
    #         return dic[key]
        
    #     return dfs()
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """ Algomonster O(len(nums) * n), o(n) """
        # Calculate the sum of all numbers in the array
        total_sum = sum(nums)
      
        # Check if the target is achievable or not
        # If the sum of nums is less than target, or the difference between sum and target
        # is not an even number, then return 0 because target can't be achieved
        if total_sum < target or (total_sum - target) % 2 != 0:
            return 0
      
        # Compute the subset sum we need to find to partition the array
        # into two subsets that give the desired target on applying + and - operations
        subset_sum = (total_sum - target) // 2
      
        # Initialize a list for dynamic programming, with a size of subset_sum + 1
        dp = [0] * (subset_sum + 1)
      
        # There is always 1 way to achieve a sum of 0, which is by selecting no elements
        dp[0] = 1
      
        # Update the dynamic programming table
        # For each number in nums, update the count of ways to achieve each sum <= subset_sum
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                # Add the number of ways to achieve a sum of j before num was considered
                dp[j] += dp[j - num]
      
        # Return the number of ways to achieve subset_sum, which indirectly gives us the number of ways
        # to achieve the target sum using '+' and '-' operations
        return dp[-1]

        
# @lc code=end



