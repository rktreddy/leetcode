#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        startCol = 0
        endCol = len(mat[0])-1
       
        while startCol <= endCol:
            maxRow = 0
            midCol = (endCol+startCol)//2
            
            for row in range(len(mat)):
                maxRow = row if (mat[row][midCol] >= mat[maxRow][midCol]) else maxRow
            
            leftIsBig    =   midCol-1 >= startCol  and  mat[maxRow][midCol-1] > mat[maxRow][midCol]
            rightIsBig   =   midCol+1 <= endCol    and  mat[maxRow][midCol+1] > mat[maxRow][midCol]
            
            if (not leftIsBig) and (not rightIsBig):   # we have found the peak element
                return [maxRow, midCol]
            elif rightIsBig:             # if rightIsBig, then there is an element in 'right' that is bigger than all the elements in the 'midCol', 
                startCol = midCol+1     # so 'midCol' cannot have 'peakPlane'
            else:                           # leftIsBig
                endCol = midCol-1
                
        return []
# @lc code=end

