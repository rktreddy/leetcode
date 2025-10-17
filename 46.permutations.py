#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach: Backtracking O(n * n!), O(n) """
    #     def backtrack(curr):
    #         if len(curr) == len(nums):
    #             ans.append(curr[:])
    #             return
            
    #         for num in nums:
    #             if num not in curr:
    #                 curr.append(num)
    #                 backtrack(curr)
    #                 curr.pop()
        
    #     ans = []
    #     backtrack([])
    #     return ans
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        """ practice: Approach: Backtracking O(n * n!), O(n) """
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
        ans = []
        backtrack([])
        return ans 


# @lc code=end

