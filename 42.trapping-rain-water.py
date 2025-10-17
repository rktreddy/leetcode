#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    # def trap(self, height):
    #     """ Approach 1: Brute force O(n^2), O(1) """
    #     ans = 0
    #     size = len(height)
    #     for i in range(1, size - 1):
    #         left_max = 0
    #         right_max = 0
    #         # Search the left part for max bar size
    #         for j in range(i, -1, -1):
    #             left_max = max(left_max, height[j])
    #         # Search the right part for max bar size
    #         for j in range(i, size):
    #             right_max = max(right_max, height[j])
    #         ans += min(left_max, right_max) - height[i]
    #     return ans
    
    # def trap(self, height: List[int]) -> int:
    #     """ Approach 2: Dynamic Programming O(n), O(n) """
    #     # Case of empty height list
    #     if len(height) == 0:
    #         return 0
    #     ans = 0
    #     size = len(height)
    #     # Create left and right max arrays
    #     left_max, right_max = [0] * size, [0] * size
    #     # Initialize first height into left max
    #     left_max[0] = height[0]
    #     for i in range(1, size):
    #         # update left max with current max
    #         left_max[i] = max(height[i], left_max[i - 1])
    #     # Initialize last height into right max
    #     right_max[size - 1] = height[size - 1]
    #     for i in range(size - 2, -1, -1):
    #         # update right max with current max
    #         right_max[i] = max(height[i], right_max[i + 1])
    #     # Calculate the trapped water
    #     for i in range(1, size - 1):
    #         ans += min(left_max[i], right_max[i]) - height[i]
    #     # Return amount of trapped water
    #     return ans
    
    # def trap(self, height):
    #     """ Approach 3: Using stacks O(n), O(n) """
    #     ans = 0
    #     current = 0
    #     st = []
    #     while current < len(height):
    #         while len(st) != 0 and height[current] > height[st[-1]]:
    #             top = st[-1]
    #             st.pop()
    #             if len(st) == 0:
    #                 break
    #             distance = current - st[-1] - 1
    #             bounded_height = (
    #                 min(height[current], height[st[-1]]) - height[top]
    #             )
    #             ans += distance * bounded_height
    #         st.append(current)
    #         current += 1
    #     return ans
    
    # def trap(self, height):
    #     """ Approach 4: Using 2 pointers O(n), O(1) """
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     left, right = 0, len(height) - 1
    #     ans = 0
    #     left_max, right_max = 0, 0
    #     while left < right:
    #         if height[left] < height[right]:
    #             left_max = max(left_max, height[left])
    #             ans += left_max - height[left]
    #             left += 1
    #         else:
    #             right_max = max(right_max, height[right])
    #             ans += right_max - height[right]
    #             right -= 1
    #     return ans
    
    # def trap(self, height):
    #     """ practice: Approach 4: Using 2 pointers O(n), O(1) """
    #     left, right = 0, len(height) - 1
    #     ans = 0
    #     left_max, right_max = 0, 0
    #     while left < right:
    #         if height[left] < height[right]:
    #             left_max = max(left_max, height[left])
    #             ans += left_max - height[left]
    #             left += 1
    #         else:
    #             right_max = max(right_max, height[right])
    #             ans += right_max - height[right]
    #             right -= 1
    #     return ans
    
    def trap(self, height):
        """ practice: Approach 4: Using 2 pointers O(n), O(1) """
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            if height(left) < height(right):
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans


# @lc code=end