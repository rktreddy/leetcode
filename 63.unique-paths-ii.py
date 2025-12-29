#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])

    #     # If the starting cell has an obstacle, then simply return as there would be
    #     # no paths to the destination.
    #     if obstacleGrid[0][0] == 1:
    #         return 0

    #     # Number of ways of reaching the starting cell = 1.
    #     obstacleGrid[0][0] = 1

    #     # Filling the values for the first column
    #     for i in range(1, m):
    #         obstacleGrid[i][0] = int(
    #             obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1
    #         )

    #     # Filling the values for the first row
    #     for j in range(1, n):
    #         obstacleGrid[0][j] = int(
    #             obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1
    #         )

    #     # Starting from cell(1,1) fill up the values
    #     # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
    #     # i.e. From above and left.
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if obstacleGrid[i][j] == 0:
    #                 obstacleGrid[i][j] = (
    #                     obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
    #                 )
    #             else:
    #                 obstacleGrid[i][j] = 0

    #     # Return value stored in rightmost bottommost cell. That is the destination.
    #     return obstacleGrid[m - 1][n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """ cracking faang O(M N), O(M N) """
        if obstacleGrid[-1][-1] == 1:
            return 0
        elif len(obstacleGrid) == 1:
            return 1 if 1 not in obstacleGrid[0] else 0
        
        self.memo = {}
        self.dfs(obstacleGrid, 0, 0)
        return self.memo[(0, 0)]
    
    def dfs(self, grid, m, n):
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        if m == len(grid) - 1 and n == len(grid[m]) - 1:
            return 1
        if (0 <= m < len(grid)) and (0 <= n < len(grid[m])) and grid[m][n] == 0:
            self.memo[(m, n)] = self.dfs(grid, m + 1, n) + self.dfs(grid, m, n + 1)
        else:
            self.memo[(m, n)] = 0
        return self.memo[(m, n)]


# @lc code=end

# """ Approach 1: Dynamic Programming O(M  N), O(1) """

