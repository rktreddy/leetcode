#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from math import factorial
class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     """ Approach 1: Dynamic Programming O(N x M), O(N x M) """
    #     d = [[1] * n for _ in range(m)]

    #     for col in range(1, m):
    #         for row in range(1, n):
    #             d[col][row] = d[col - 1][row] + d[col][row - 1]

    #     return d[m - 1][n - 1]
        
    # def uniquePaths(self, m: int, n: int) -> int:
    #     """ Approach 2: Math (Python3 only) O((M+N) log(M+N)log log(M+N)^2), O(1)"""
    #     return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
    
    def uniquePaths(self, m: int, n: int) -> int:
        """ cracking faang: grid traversal DFS + Memoization O(N x M), O(N x M) """
        self.memo = {}
        self.memo[(m - 1, n - 1)] = 1
        self.dfs(m, n, 0, 0)
        return self.memo[(0, 0)]
    
    def dfs(self, m, n, x, y):
        if (x, y) in self.memo:
            return self.memo[(x, y)]
        if (0 <= x < m) and (0 <= y < n):
            self.memo[(x, y)] = self.dfs(m, n, x + 1, y) + self.dfs(m, n, x, y + 1)
            return self.memo[(x, y)]
        else:
            return 0
        
    

# @lc code=end

