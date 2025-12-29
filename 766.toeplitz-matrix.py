#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """ Approach 1: Group by Category O(M * N), O(M + N) """
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

   
# @lc code=end

# def isToeplitzMatrix(self, matrix):
    #     """ Approach 2: Compare With Top-Left Neighbor O(M * N), O(1) """
    #     return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
    #                for r, row in enumerate(matrix)
    #                for c, val in enumerate(row))

    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     """ Approach 1: Group by Category O(M * N), O(M + N) """
    #     groups = {}
    #     for r, row in enumerate(matrix):
    #         for c, val in enumerate(row):
    #             if r-c not in groups:
    #                 groups[r-c] = val
    #             elif groups[r-c] != val:
    #                 return False
    #     return True

    #  def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     """ Cracking Faang: Group by Category O(M * N), O(1) """
    #     def is_diagonal_univalue(row, col):
    #         val = matrix[row][col]
    #         while row < len(matrix) and col < len(matrix[0]):
    #             if matrix[row][col] != val:
    #                 return False
    #             row += 1
    #             col += 1
    #         return True
        
    #     for col in range(len(matrix[0])):
    #         if not is_diagonal_univalue(0, col):
    #             return False
    #     for row in range(len(matrix)):
    #         if not is_diagonal_univalue(row, 0):
    #             return False
    #     return True
        