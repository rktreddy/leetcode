#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    #     row, col = len(image), len(image[0])
    #     new_color = image[sr][sc]
    #     if new_color == color:
    #         return image
    #     def dfs(r, c):
    #         if image[r][c] == new_color:
    #             image[r][c] == color
    #             if r >= 1:
    #                 dfs(r-1, c)
    #             if r + 1 < row:
    #                 dfs(r+1, c)
    #             if c >= 1:
    #                 dfs(r, c-1)
    #             if c + 1 < col:
    #                 dfs(r, c+1)
    #     dfs(sr, sc)
    #     return image
    
    def floodFill(self, image, sr, sc, newColor):
        """ Approach #1: Depth-First Search [Accepted] O(N), O(N) """
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image
        
# @lc code=end

