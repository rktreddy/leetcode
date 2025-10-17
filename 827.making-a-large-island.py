#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    # def largestIsland(self, grid: List[List[int]]) -> int:
    #     """ Approach 1: Naive Depth First Search O(N^4), O(N^2) """
    #     N = len(grid)

    #     def check(r, c):
    #         seen = {(r, c)}
    #         stack = [(r, c)]
    #         while stack:
    #             r, c = stack.pop()
    #             for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
    #                 if (nr, nc) not in seen and 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
    #                     stack.append((nr, nc))
    #                     seen.add((nr, nc))
    #         return len(seen)

    #     ans = 0
    #     has_zero = False
    #     for r, row in enumerate(grid):
    #         for c, val in enumerate(row):
    #             if val == 0:
    #                 has_zero = True
    #                 grid[r][c] = 1
    #                 ans = max(ans, check(r, c))
    #                 grid[r][c] = 0

    #     return ans if has_zero else N*N
        
    def largestIsland(self, grid):
        """ Approach #2: Component Sizes O(N^2), O(N^2) """
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans

# @lc code=end

