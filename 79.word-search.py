#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     """ Approach 1: Backtracking O(N 3^L), O(L) """
    #     self.rows = len(board)
    #     self.cols = len(board[0])
    #     self.board = board

    #     for row in range(self.rows):
    #         for col in range(self.cols):
    #             if self.backtrack(row, col, word):
    #                 return True
    #     return False

    # def backtrack(self, row: int, col:int, suffix: str) -> bool:
    #     if len(suffix) == 0:
    #         return True
        
    #     if (
    #         row < 0
    #         or row == self.rows
    #         or col < 0
    #         or col == self.cols
    #         or self.board[row][col] != suffix[0]
    #     ):
    #         return False
        
    #     ret = False
    #     self.board[row][col] = "#"
    #     for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    #         ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
    #         if ret:
    #             break

    #     self.board[row][col] = suffix[0]

    #     return ret
        
        
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     """ Neetcode: 1. Backtracking (Hash Set) O(m 4^n), O(n) """
    #     ROWS, COLS = len(board), len(board[0])
    #     path = set()

    #     def dfs(r, c, i):
    #         if i == len(word):
    #             return True

    #         if (min(r, c) < 0 or
    #             r >= ROWS or c >= COLS or
    #             word[i] != board[r][c] or
    #             (r, c) in path):
    #             return False

    #         path.add((r, c))
    #         res = (dfs(r + 1, c, i + 1) or
    #                dfs(r - 1, c, i + 1) or
    #                dfs(r, c + 1, i + 1) or
    #                dfs(r, c - 1, i + 1))
    #         path.remove((r, c))
    #         return res

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if dfs(r, c, 0):
    #                 return True
    #     return False
    

    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     """ Neetcode: 2. Backtracking (Visited Array) O(m 4^n), O(n) """
    #     ROWS, COLS = len(board), len(board[0])
    #     visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

    #     def dfs(r, c, i):
    #         if i == len(word):
    #             return True
    #         if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
    #             word[i] != board[r][c] or visited[r][c]):
    #             return False

    #         visited[r][c] = True
    #         res = (dfs(r + 1, c, i + 1) or
    #                dfs(r - 1, c, i + 1) or
    #                dfs(r, c + 1, i + 1) or
    #                dfs(r, c - 1, i + 1))
    #         visited[r][c] = False
    #         return res

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if dfs(r, c, 0):
    #                 return True
    #     return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        """ Neetcode: 3. Backtracking (Optimal) O(m 4^n), O(n) """

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False



# @lc code=end

