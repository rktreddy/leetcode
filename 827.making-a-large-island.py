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
        
    # def largestIsland(self, grid):
    #     """ Approach #2: Component Sizes O(N^2), O(N^2) """
    #     N = len(grid)

    #     def neighbors(r, c):
    #         for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
    #             if 0 <= nr < N and 0 <= nc < N:
    #                 yield nr, nc

    #     def dfs(r, c, index):
    #         ans = 1
    #         grid[r][c] = index
    #         for nr, nc in neighbors(r, c):
    #             if grid[nr][nc] == 1:
    #                 ans += dfs(nr, nc, index)
    #         return ans

    #     area = {}
    #     index = 2
    #     for r in range(N):
    #         for c in range(N):
    #             if grid[r][c] == 1:
    #                 area[index] = dfs(r, c, index)
    #                 index += 1

    #     ans = max(area.values() or [0])
    #     for r in range(N):
    #         for c in range(N):
    #             if grid[r][c] == 0:
    #                 seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
    #                 ans = max(ans, 1 + sum(area[i] for i in seen))
    #     return ans
    
    def largestIsland(self, grid):
        """ Cracking Faang: Component Sizes O(N^2), O(N^2) """
        self.island_id = -1 # -ve id for each island
        self.island_areas = {}

        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                island_area = self.dfs(grid, m, n)
                self.island_areas[self.island_id] = island_area
                self.island_id -= 1

        max_area = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if not grid[m][n]:
                    area = 1

                    surrounding = set()
                    
                    for m_inc, n_inc in self.directions:
                        new_m = m + m_inc
                        new_n = n + n_inc

                        if (0 <= new_m < len(grid)) and (0 <= new_n < len(grid[0])) and grid[new_m][new_n] != 0:
                            surrounding.add(grid[new_m][new_n])
                    for island_id in surrounding:
                        area += self.island_areas[island_id]

                    max_area = max(max_area, area)

        return max_area if max_area else len(grid)**2
    
    def dfs(self, grid, m, n):
        if (0 <= m < len(grid)) and (0 <= n < len(grid[0])) and grid[m][n] == 1:
            grid[m][n] = self.island_id
            area = 1
            for m_inc, n_inc in self.directions:
                area += self.dfs(grid, m + m_inc, n + n_inc)

            return area
        else:
            return 0
        
    def largestIsland(self, grid):
        """ practice: Cracking Faang: Component Sizes O(N^2), O(N^2) """
        self.island_id = -1
        self.island_areas = {}

        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                island_area = self.dfs(grid, m, n)
                self.island_areas[self.island_id] = island_area
                self.island_id -= 1

        max_area = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if not grid[m][n]:
                    area = 1
                    surrounding = set()
                    for m_inc, n_inc in self.directions:
                        new_m = m + m_inc
                        new_n = n + n_inc
                        if (0 <= new_m < len(grid)) and (0 <= new_n < len(grid[0])) and grid[new_m][new_n] != 0:
                            surrounding.add(grid[new_m][new_n])

                    for island_id in surrounding:
                        area += self.island_areas[island_id]

                    max_area = max(max_area, area)

        return max_area if max_area else len(grid) ** 2

    def dfs(self, grid, m, n):
        if (0 <= m < len(grid)) and (0 <= n < len(grid[0])) and grid[m][n] == 1:
            grid[m][n] = self.island_id
            area = 1
            for m_inc, n_inc in self.directions:
                area += self.dfs(grid, m + m_inc, n + n_inc)
            return area
        else:
            return 0

                

# @lc code=end

