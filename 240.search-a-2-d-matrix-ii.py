#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     """ Approach 1: Brute Force O(mn), O(1) """
    #     for row in matrix:
    #         if target in row:
    #             return True
        
    #     return False
    
    # def binary_search(self, matrix, target, start, vertical):
    #     lo = start
    #     hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

    #     while hi >= lo:
    #         mid = (lo + hi) // 2
    #         if vertical: # searching a column
    #             if matrix[start][mid] < target:
    #                 lo = mid + 1
    #             elif matrix[start][mid] > target:
    #                 hi = mid - 1
    #             else:
    #                 return True
    #         else: # searching a row
    #             if matrix[mid][start] < target:
    #                 lo = mid + 1
    #             elif matrix[mid][start] > target:
    #                 hi = mid - 1
    #             else:
    #                 return True
        
    #     return False

    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     """ Approach 2: Binary Search O(log(n!)), O(1) """
    #     # an empty matrix obviously does not contain `target`
    #     if not matrix:
    #         return False

    #     # iterate over matrix diagonals starting in bottom left.
    #     for i in range(min(len(matrix), len(matrix[0]))):
    #         vertical_found = self.binary_search(matrix, target, i, True)
    #         horizontal_found = self.binary_search(matrix, target, i, False)
    #         if vertical_found or horizontal_found:
    #             return True
        
    #     return False
    
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     """ Approach 3: Divide and Conquer O(nlogn), O(logn) """
    #     # an empty matrix obviously does not contain `target`
    #     if not matrix:
    #         return False

    #     def search_rec(left, up, right, down):
    #         # this submatrix has no height or no width.
    #         if left > right or up > down:
    #             return False
    #         # `target` is already larger than the largest element or smaller
    #         # than the smallest element in this submatrix.
    #         elif target < matrix[up][left] or target > matrix[down][right]:
    #             return False

    #         mid = left + (right-left) // 2

    #         # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
    #         row = up
    #         while row <= down and matrix[row][mid] <= target:
    #             if matrix[row][mid] == target:
    #                 return True
    #             row += 1
            
    #         return search_rec(left, row, mid - 1, down) or \
    #                search_rec(mid + 1, up, right, row - 1)

    #     return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ Approach 4: Search Space Reduction O(m + n), O(1) """
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False
        
# @lc code=end

