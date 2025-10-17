#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """ Approach 1: Breadth-First Search (BFS) O(m . n), O(m . n) """
        # def valid(row, col):
        #     return 0 <= row < m and 0 <= col < n 
        
        # matrix = [row[:] for row in mat]
        # m = len(matrix)
        # n = len(matrix[0])
        # queue = deque()
        # seen = set()

        # for row in range(m):
        #     for col in range(n):
        #         if matrix[row][col] == 0:
        #             queue.append((row, col, 0))
        #             seen.add((row, col))

        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # while queue:
        #     row, col, steps = queue.popleft()

        #     for dx, dy in directions:
        #         next_row, next_col = row + dy, col + dx
        #         if (next_row, next_col) not in seen and valid(next_row, next_col):
        #             seen.add((next_row, next_col))
        #             queue.append((next_row, next_col, steps + 1))
        #             matrix[next_row][next_col] = steps + 1

        # return matrix
        
        """ Approach 2: Dynamic Programming O(m . n), O(m . n) """
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])

        for row in range(m):
            for col in range(n):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row > 0:
                        min_neighbor = min(min_neighbor, dp[row - 1] [col])
                    if col > 0:
                        min_neighbor = min(min_neighbor, dp[row] [col-1])

                    dp[row][col] = min_neighbor + 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row < m - 1:
                        min_neighbor = min(min_neighbor, dp[row + 1][col])
                    if col < n - 1:
                        min_neighbor = min(min_neighbor, dp[row][col + 1])

                    dp[row][col] = min(dp[row][col], min_neighbor + 1)
        return dp
                                           

# @lc code=end

