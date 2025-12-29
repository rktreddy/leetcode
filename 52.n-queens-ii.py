#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        """ Approach: Backtracking O(N!), O(N^2) """
        def backtrack(row):
            if row == n:
                nonlocal count
                count += 1
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

        count = 0
        queens = {}
        columns = set()
        diagonals1 = set()
        diagonals2 = set()
        backtrack(0)
        return count
        
# @lc code=end

