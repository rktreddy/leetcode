#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#
import random
# @lc code=start
class Solution:
    """ cracking faang: reservoir sampling O(N), O(a) """

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def pick(self, target: int) -> int:
        count = 0
        picked_index = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1

                if random.randint(1, count) == count:
                    picked_index = i
        return picked_index
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

