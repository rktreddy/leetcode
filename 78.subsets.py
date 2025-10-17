#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach 1: Cascading O(N * 2^N), O(N * 2^N) """
    #     output = [[]]

    #     for num in nums:
    #         output += [curr + [num] for curr in output]

    #     return output
    
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach 2: Backtracking O(N * 2^N), O(N) """
    #     def backtrack(first=0, curr=[]):
    #         # If the combination is done
    #         if len(curr) == k:
    #             output.append(curr[:])
    #             return
    #         for i in range(first, n):
    #             # Add nums[i] into the current combination
    #             curr.append(nums[i])

    #             # Use the next integers to complete the combination
    #             backtrack(i + 1, curr)

    #             # Backtrack
    #             curr.pop()

    #     output = []
    #     n = len(nums)
    #     for k in range(n + 1):
    #         backtrack()
    #     return output
    
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach 3: Lexicographic (Binary Sorted) Subsets O(N * 2^N), O(N) """
    #     n = len(nums)
    #     output = []

    #     for i in range(2 ** n, 2 ** (n + 1)):
    #         bitmask = bin(i)[3:]
    #         output.append([nums[j] for j in range(n) if bitmask[j] == "1"])

    #     return output
    
    # """ Top upvoted solutions O(N * 2^N), O(N) """
    # def subsets(self, nums):
    #     ret = []
    #     self.dfs(nums, [], ret)
    #     return ret
    
    # def dfs(self, nums, path, ret):
    #     ret.append(path)
    #     for i in range(len(nums)):
    #         self.dfs(nums[i+1:], path+[nums[i]], ret)

    # """ practice: Top upvoted solutions """
    # def subsets(self, nums):
    #     ret = []
    #     self.dfs(nums, [], ret)
    #     return ret 
    
    # def dfs(self, nums, path, ret):
    #     ret.append(path)
    #     for i in range(len(nums)):
    #         self.dfs(nums[i+1:], path + [nums[i]], ret)
        
       
    # # Bit Manipulation  O(N * 2^N), O(N)
    # def subsets2(self, nums):
    #     res = []
    #     nums.sort()
    #     for i in xrange(1<<len(nums)):
    #         tmp = []
    #         for j in xrange(len(nums)):
    #             if i & 1 << j:  # if i >> j & 1:
    #                 tmp.append(nums[j])
    #         res.append(tmp)
    #     return res
		
    # # Iteratively O(N * 2^N), O(N)
    # def subsets(self, nums):
    #     res = [[]]
    #     for num in sorted(nums):
    #         res += [item+[num] for item in res]
    #     return res
    
    # practice: Iteratively O(N * 2^N), O(N)
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res
        
# @lc code=end

