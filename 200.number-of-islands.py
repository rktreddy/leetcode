#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     """ Approach #1 DFS [Accepted] O(M * N), O(M * N) """
    #     if not grid:
    #         return 0
        
    #     num_islands = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == "1":
    #                 self.dfs(grid, i, j)
    #                 num_islands += 1
        
    #     return num_islands
    
    # def dfs(self, grid, r, c):
    #     if (
    #         r < 0
    #         or c < 0
    #         or r >= len(grid)
    #         or c >= len(grid[0])
    #         or grid[r][c] != "1"
    #     ):
    #         return
    #     grid[r][c] = "0"
    #     self.dfs(grid, r - 1, c)
    #     self.dfs(grid, r + 1, c)
    #     self.dfs(grid, r, c - 1)
    #     self.dfs(grid, r, c + 1)

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     """ Approach #2: BFS [Accepted] O(M x N), O(min (M, N))"""
    #     if not grid:
    #         return 0
        
    #     nr = len(grid)
    #     nc = len(grid[0])
    #     num_islands = 0

    #     for r in range(nr):
    #         for c in range(nc):
    #             if grid[r][c] == "1":
    #                 num_islands += 1
    #                 grid[r][c] = 0 # mark as visited
    #                 neighbors = []
    #                 neighbors.append((r, c))
    #                 while neighbors:
    #                     row, col = neighbors.pop(0)
    #                     if row - 1 >= 0 and grid[row - 1][col] == "1":
    #                         neighbors.append((row - 1, col))
    #                         grid[row - 1][col] = "0"
    #                     if row + 1 < nr and grid[row + 1][col] == "1":
    #                         neighbors.append((row + 1, col))
    #                         grid[row + 1][col] = "0"
    #                     if col - 1 >= 0 and grid[row][col - 1] == "1":
    #                         neighbors.append((row, col - 1))
    #                         grid[row][col - 1] = "0"
    #                     if col + 1 < nc and grid[row][col + 1] == "1":
    #                         neighbors.append((row, col + 1))
    #                         grid[row][col + 1] = "0"
    #     return num_islands
        
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     """ practice: Approach #2: BFS [Accepted] O(M x N), O(min (M, N)) """
    #     if not grid:
    #         return 0
        
    #     nr, nc = len(grid), len(grid[0])
    #     num_islands = 0

    #     for r in range(nr):
    #         for c in range(nc):
    #             if grid[r][c] == "1":
    #                 grid[r][c] = "0"
    #                 num_islands += 1
    #                 neighnors = []
    #                 neighnors.append((r, c))
    #                 while neighnors:
    #                     row, col = neighnors.pop()
    #                     if row - 1 >= 0 and grid[row - 1][col] == "1":
    #                         grid[row - 1][col] = "0"
    #                         neighnors.append((row - 1, col))
    #                     if row + 1 < nr and grid[row + 1][col] == "1":
    #                         grid[row + 1][col] = "0"
    #                         neighnors.append((row + 1, col))
    #                     if col - 1 >= 0 and grid[row][col - 1] == "1":
    #                         grid[row][col - 1] = "0"
    #                         neighnors.append((row, col - 1))
    #                     if col + 1 < nc and grid[row][col + 1] == "1":
    #                         grid[row][col + 1] = "0"
    #                         neighnors.append((row, col + 1))

    #     return num_islands
    
    def numIslands(self, grid: List[List[str]]) -> int:
        """ practice: Approach #2: BFS [Accepted] O(M x N), O(min (M, N)) """
        if not grid:
            return 0
        nr, nc = len(grid), len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    num_islands += 1
                    neighbors = []
                    neighbors.append((r, c))
                    while neighbors:
                        row, col = neighbors.pop()
                        if row - 1 >= 0 and grid[row -1][col] == '1':
                            grid[row - 1][col] = '0'
                            neighbors.append((row - 1, col))
                        if row + 1 < nr and grid[row + 1][col] == '1':
                            grid[row + 1][col] = '0'
                            neighbors.append((row + 1, col))
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            grid[row][col - 1] = '0'
                            neighbors.append((row - 1, col))
                        if col + 1 < nc and grid[row][col + 1] == '1':
                            grid[row][col + 1] = '0'
                            neighbors.append((row, col + 1))
        return num_islands

                
    


# class UnionFind:
#     def __init__(self, grid):
#         self.count = 0
#         m, n = len(grid), len(grid[0])
#         self.parent = []
#         self.rank = []
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     self.parent.append(i * n + j)
#                     self.count += 1
#                 else:
#                     self.parent.append(-1)
#                 self.rank.append(0)

#     def find(self, i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]

#     def union(self, x, y):
#         rootx = self.find(x)
#         rooty = self.find(y)
#         if rootx != rooty:
#             if self.rank[rootx] > self.rank[rooty]:
#                 self.parent[rooty] = rootx
#             elif self.rank[rootx] < self.rank[rooty]:
#                 self.parent[rootx] = rooty
#             else:
#                 self.parent[rooty] = rootx
#                 self.rank[rootx] += 1
#             self.count -= 1

#     def getCount(self):
#         return self.count


# class Solution:
#     """ Approach #3: Union Find (aka Disjoint Set) [Accepted] O(M x N), O(M x N)"""
#     def numIslands(self, grid):
#         if not grid or not grid[0]:
#             return 0

#         nr = len(grid)
#         nc = len(grid[0])
#         uf = UnionFind(grid)

#         for r in range(nr):
#             for c in range(nc):
#                 if grid[r][c] == "1":
#                     grid[r][c] = "0"
#                     if r - 1 >= 0 and grid[r - 1][c] == "1":
#                         uf.union(r * nc + c, (r - 1) * nc + c)
#                     if r + 1 < nr and grid[r + 1][c] == "1":
#                         uf.union(r * nc + c, (r + 1) * nc + c)
#                     if c - 1 >= 0 and grid[r][c - 1] == "1":
#                         uf.union(r * nc + c, r * nc + c - 1)
#                     if c + 1 < nc and grid[r][c + 1] == "1":
#                         uf.union(r * nc + c, r * nc + c + 1)

#         return uf.getCount()
        
# @lc code=end

