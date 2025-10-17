#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     """ Approach 3: One-pass Hash Table O(n), O(n) """
    #     hashMap = {}

    #     for i, n in enumerate(nums):
    #         diff = target - n
    #         if diff in hashMap:
    #             return [hashMap[diff], i]
    #         hashMap[n] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ practice """
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[n] = i

        
        
# @lc code=end


def twoSum(self, nums: List[int], target: int) -> List[int]:
    """ practice: if target is difference """
    hashmap = {}
    for i, n in enumerate(nums):
        diff = abs(target + n)
        if diff in hashmap:
            return [i, hashmap[diff]]
        hashmap[n] = i