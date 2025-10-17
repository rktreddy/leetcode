#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     hashmap = {}
    #     for i, num in enumerate(nums):
    #         if num in hashmap and abs(i - hashmap[num]) <= k:
    #             return True
    #         hashmap[num] = i
    #     return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """ practice O(n), O(n) """
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap and abs(i - hashmap[num]) <= k:
                return True
            hashmap[num] = i
        return False

# @lc code=end

