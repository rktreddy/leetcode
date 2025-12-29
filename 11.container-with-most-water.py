#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     """ my initial try """
    #     left, right = 0, len(height) - 1

    #     max_water = 0
    #     while left < right:
    #         water = min(height[left], height[right]) * (right - left)
    #         max_water = max(max_water, water)
    #         left += 1
    #         right -= 1

    #     return max_water

    # def maxArea(self, height: List[int]) -> int:
    #     """ Approach 1: Brute Force O(n^2), O(1) """
    #     maxarea = 0
    #     for left in range(len(height)):
    #         for right in range(left + 1, len(height)):
    #             width = right - left
    #             maxarea = max(maxarea, min(height[left], height[right]) * width)

    #     return maxarea
    
    # def maxArea(self, height: List[int]) -> int:
    #     """ Approach 2: Two Pointer Approach O(n), O(1) """
    #     maxarea = 0
    #     left, right = 0, len(height) - 1
    #     while left < right:
    #         width = right - left
    #         maxarea = max(maxarea, min(height[left], height[right]) * width)
    #         if height[left] <= height[right]:
    #             left += 1
    #         else:
    #             right -= 1
    #     return maxarea
    
    def maxArea(self, height: List[int]) -> int:
        """ Practice: Approach 2: Two Pointer Approach O(n), O(1) """
        maxarea = 0
        l, r = 0, len(height) - 1
        while l < r:
            width = r - l
            maxarea = max(maxarea, min(height[l], height[r]) * width)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxarea


# @lc code=end

