#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     """ Approach #3 (Hash Table) [Accepted] O(n), O(n) """
    #     hashset = set()

    #     for num in nums:
    #         if num in hashset:
    #             return True
    #         else:
    #             hashset.add(num)
    #     return False
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        """ practice: Approach #3 (Hash Table) [Accepted] O(n), O(n) """
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False
    
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(set(nums)) < len(nums)
        
# @lc code=end

