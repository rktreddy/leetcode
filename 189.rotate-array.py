#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     for i in range(k):
    #         last = nums[n - 1]
    #         for j in range(n - 1, -1, -1):
    #             nums[j] = nums[j - 1]
    #         nums[0] = last
    #     return nums
        
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """ Approach 1: Brute Force O(n k), O(1) """
    #     # speed up the rotation
    #     k %= len(nums)

    #     for i in range(k):
    #         previous = nums[-1]
    #         for j in range(len(nums)):
    #             nums[j], previous = previous, nums[j]

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """ Approach 2: Using Extra Array O(n), O(n) """
    #     n = len(nums)
    #     a = [0] * n
    #     for i in range(n):
    #         a[(i + k) % n] = nums[i]
    #     nums[:] = a


    # def rotate(self, nums: List[int], k: int) -> None:
    #     """ Approach 3: Using Cyclic Replacements O(n), O(1) """
    #     n = len(nums)
    #     k %= n

    #     start = count = 0
    #     while count < n:
    #         current, prev = start, nums[start]
    #         while True:
    #             next_idx = (current + k) % n
    #             nums[next_idx], prev = prev, nums[next_idx]
    #             current = next_idx
    #             count += 1

    #             if start == current:
    #                 break
    #         start += 1

    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        """ Approach 4: Using Reverse O(n), O(1) """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
# @lc code=end

