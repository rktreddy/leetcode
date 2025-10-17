#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     """ Approach 1: Brute Force O(n^3), O(1)"""
    #     max_area = 0
    #     for i in range(len(heights)):
    #         for j in range(i, len(heights)):
    #             min_height = inf
    #             for k in range(i, j + 1):
    #                 min_height = min(min_height, heights[k])
    #             max_area = max(max_area, min_height * (j - i + 1))
    #     return max_area    

        
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     """ Approach 2: Better Brute Force O(n^2), O(1) """
    #     max_area = 0
    #     for i in range(len(heights)):
    #         min_height = inf
    #         for j in range(i, len(heights)):
    #             min_height = min(min_height, heights[j])
    #             max_area = max(max_area, min_height * (j - i + 1))
    #     return max_area
    
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     """ Approach 3: Divide and Conquer Approach O(n log n) to O(n^2), O(n)"""
    #     def calculateArea(heights: List[int], start: int, end: int) -> int:
    #         if start > end:
    #             return 0
    #         min_index = start
    #         for i in range(start, end + 1):
    #             if heights[min_index] > heights[i]:
    #                 min_index = i
    #         return max(
    #             heights[min_index] * (end - start + 1),
    #             calculateArea(heights, start, min_index - 1),
    #             calculateArea(heights, min_index + 1, end),
    #         )

    #     return calculateArea(heights, 0, len(heights) - 1)
    
    """ Approach 4: Better Divide and Conquer O(n log n), O(n) """

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     """ Approach 5: Using Stack O(n), O(n) """
    #     stack = [-1]
    #     max_area = 0
    #     for i in range(len(heights)):
    #         while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
    #             current_height = heights[stack.pop()]
    #             current_width = i - stack[-1] - 1
    #             max_area = max(max_area, current_height * current_width)
    #         stack.append(i)

    #     while stack[-1] != -1:
    #         current_height = heights[stack.pop()]
    #         current_width = len(heights) - stack[-1] - 1
    #         max_area = max(max_area, current_height * current_width)
            
    #     return max_area
    
    # def largestRectangleArea/(self, heights: List[int]) -> int:
    #     """ Top voted solution """
    #     heights.append(0)
    #     stack = [-1]
    #     ans = 0
    #     for i in range(len(heights)):
    #         while heights[i] < heights[stack[-1]]:
    #             h = heights[stack.pop()]
    #             w = i - stack[-1] - 1
    #             ans = max(ans, h * w)
    #         stack.append(i)
    #     heights.pop()
    #     return ans
      
              
    def largestRectangleArea(self, heights: list[int]) -> int:
        ans = 0
        stack = []

        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, h * w)
            stack.append(i)

        return ans

# @lc code=end

