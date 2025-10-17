#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap and abs(i - hashmap[num]) <= indexDiff and abs(num - )
        
# @lc code=end

