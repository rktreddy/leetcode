#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
# class NumArray:
    # O(n), O(n)

    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     cum_sum = [0] * len(self.nums)
    #     cum_sum[0] = self.nums[0]
    #     for i in range(1, len(self.nums)):
    #         cum_sum[i] += cum_sum[i - 1] + self.nums[i]
    #     return cum_sum[right] - cum_sum[left] + self.nums[left]

    # def __init__(self, nums: List[int]):
    #     self.sum = []
    #     sum_till = 0
    #     for i in nums:
    #         sum_till += i
    #         self.sum.append(sum_till)

    # def sumRange(self, i: int, j: int) -> int:
    #     if i > 0 and j > 0:
    #         return self.sum[j] - self.sum[i - 1]
    #     else:
    #         return self.sum[i or j]
        
from itertools import accumulate

class NumArray:
    def __init__(self, nums: List[int]):
        # Pre-calculate the cumulative sum of the array.
        # The 'initial=0' makes sure the sum starts from index 0 for easier calculations.
        self.cumulative_sum = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum of elements between 'left' and 'right'
        # by subtracting the sum up to 'left' from the sum up to 'right + 1'.
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

