#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     """ Approach 1: Hash Set O(N^2), O(N^2) """
    #     N = 9

    #     # Use hash set to record the status
    #     rows = [set() for _ in range(N)]
    #     cols = [set() for _ in range(N)]
    #     boxes = [set() for _ in range(N)]

    #     for r in range(N):
    #         for c in range(N):
    #             val = board[r][c]
    #             # Check if the position is filled with number
    #             if val == ".":
    #                 continue

    #             # Check the row
    #             if val in rows[r]:
    #                 return False
    #             rows[r].add(val)

    #             # Check the column
    #             if val in cols[c]:
    #                 return False
    #             cols[c].add(val)

    #             # Check the box
    #             idx = (r // 3) * 3 + c // 3
    #             if val in boxes[idx]:
    #                 return False
    #             boxes[idx].add(val)

    #     return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ Practice: Approach 1: Hash Set O(N^2), O(N^2) """
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True
        

    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     """ Approach 1: Hash Set O(N^2), O(N^2) """
    #     N = 9

    #     # Use an array to record the status
    #     rows = [[0] * N for _ in range(N)]
    #     cols = [[0] * N for _ in range(N)]
    #     boxes = [[0] * N for _ in range(N)]

    #     for r in range(N):
    #         for c in range(N):
    #             # Check if the position is filled with number
    #             if board[r][c] == ".":
    #                 continue

    #             pos = int(board[r][c]) - 1

    #             # Check the row
    #             if rows[r][pos] == 1:
    #                 return False
    #             rows[r][pos] = 1

    #             # Check the column
    #             if cols[c][pos] == 1:
    #                 return False
    #             cols[c][pos] = 1

    #             # Check the box
    #             idx = (r // 3) * 3 + c // 3
    #             if boxes[idx][pos] == 1:
    #                 return False
    #             boxes[idx][pos] = 1

    #     return True
        
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     """ Approach 1: Hash Set O(N^2), O(N) """
    #     N = 9
    #     # Use binary number to check previous occurrence
    #     rows = [0] * N
    #     cols = [0] * N
    #     boxes = [0] * N

    #     for r in range(N):
    #         for c in range(N):
    #             # Check if the position is filled with number
    #             if board[r][c] == ".":
    #                 continue

    #             pos = int(board[r][c]) - 1

    #             # Check the row
    #             if rows[r] & (1 << pos):
    #                 return False
    #             rows[r] |= 1 << pos

    #             # Check the column
    #             if cols[c] & (1 << pos):
    #                 return False
    #             cols[c] |= 1 << pos

    #             # Check the box
    #             idx = (r // 3) * 3 + c // 3
    #             if boxes[idx] & (1 << pos):
    #                 return False
    #             boxes[idx] |= 1 << pos

    #     return True
    
# @lc code=end

