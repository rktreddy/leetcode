#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """ Approach: Backtracking O(N!), O(N^2) """
        def backtrack(row):
            if row == n:
                board = []
                for i in range(n):
                    row_str = ''.join('Q' if j == queens[i] else '.' for j in range(n))
                    board.append(row_str)
                result.append(board)
                return
            
            for col in range(n):
                if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue
                
                queens[row] = col
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                backtrack(row + 1)

                del queens[row]
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        result = []
        queens = {}
        columns = set()
        diagonals1 = set()
        diagonals2 = set()
        backtrack(0)
        return result
        
# @lc code=end

