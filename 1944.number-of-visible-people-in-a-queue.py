#
# @lc app=leetcode id=1944 lang=python3
#
# [1944] Number of Visible People in a Queue
#

# @lc code=start
class Solution:
    # def canSeePersonsCount(self, heights: List[int]) -> List[int]:
    #     """ my first attempt O(n), O(n) """
    #     max_height = 0
    #     cur_num = 0
    #     res = [0]
    #     for i in range(len(heights) - 2, -1, -1):
    #         if heights[i] > max_height:
    #             cur_num += 1
    #             max_height = heights[i]
    #         else:
    #             cur_num = 0
    #         res.append(cur_num)
    #     return res
    
    # def canSeePersonsCount(self, heights: List[int]) -> List[int]:
    #     """ cracking faang: monotonic stack: O(N), O(N) """
    #     N = len(heights)
    #     res = [0] * N
    #     stack = []
    #     for i in range(N - 1, -1, -1):
    #         height = heights[i]
    #         visible = 0
    #         while stack and height > stack[-1]:
    #             visible += 1
    #             stack.pop()
    #         if stack:
    #             visible += 1

    #         res[i] = visible
    #         stack.append(height)
    #     return res
            
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """ pratcie: cracking faang: monotonic stack: O(N), O(N) """
        N = len(heights)
        res = [0] * N
        stack = []
        for i in range(N - 1, -1, -1):
            height = heights[i]
            visible = 0
            while stack and height > stack[-1]:
                visible += 1
                stack.pop()
            if stack:
                visible += 1
            res[i] = visible
            stack.append(height)
        return res
        
# @lc code=end

