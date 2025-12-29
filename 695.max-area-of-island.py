#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     """ modify leetcode 200: BFS [Accepted] O(M x N), O(min (M, N)) """
    #     if not grid:
    #         return 0
    #     nr, nc = len(grid), len(grid[0])
    #     # num_islands = 0
    #     maxarea = 0 
    #     for r in range(nr):
    #         for c in range(nc):
    #             currarea = 0
    #             if grid[r][c] == '1':
    #                 grid[r][c] = '0'
    #                 # num_islands += 1
    #                 neighbors = []
    #                 neighbors.append((r, c))
    #                 while neighbors:
    #                     currarea += 1
    #                     row, col = neighbors.pop()
    #                     if row - 1 >= 0 and grid[row -1][col] == '1':
    #                         grid[row - 1][col] = '0'
    #                         neighbors.append((row - 1, col))
    #                     if row + 1 < nr and grid[row + 1][col] == '1':
    #                         grid[row + 1][col] = '0'
    #                         neighbors.append((row + 1, col))
    #                     if col - 1 >= 0 and grid[row][col - 1] == '1':
    #                         grid[row][col - 1] = '0'
    #                         neighbors.append((row, col - 1))
    #                     if col + 1 < nc and grid[row][col + 1] == '1':
    #                         grid[row][col + 1] = '0'
    #                         neighbors.append((row, col + 1))
    #             maxarea = max(maxarea, currarea)
    #     return maxarea
    

    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     """ cracking faang: modify leetcode 200: BFS [Accepted] O(M x N), O(min (M, N)) """
    #     max_area = 0
    #     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    #     def find_area(grid, row, col):
    #         if (0 <= row < len(grid)) and (0<= col < len(grid[0])) and grid[row][col] == 1:
    #             grid[row][col] = 0
    #             area = 1
    #             for dr, dc in directions:
    #                 area += find_area(grid, row + dr, col + dc)
    #             return area
    #         else:
    #             return 0

    #     for row in range(len(grid)):
    #         for col in range(len(grid[0])):
    #             area = find_area(grid, row, col)
    #             max_area = max(max_area, area)
    #     return max_area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """ practice: cracking faang: modify leetcode 200: BFS [Accepted] O(M x N), O(min (M, N)) """
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def find_area(grid, r, c):
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == 1:
                grid[r][c] = 0

                area = 1
                for dr, dc in directions:
                    area += find_area(grid, r + dr, c + dc)
                return area
            else:
                return 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                area = find_area(grid, row, col)
                max_area = max(max_area, area)
        return max_area

        
# @lc code=end

