#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     """ Approach 1: Prefix Sum and Hashing O(n), O(n)"""
    #     prefix_mod = 0
    #     mod_seen = {0: -1}

    #     for i in range(len(nums)):
    #         prefix_mod = (prefix_mod + nums[i]) % k

    #         if prefix_mod in mod_seen:
    #             if i - mod_seen[prefix_mod] > 1:
    #                 return True
    #         else:
    #             mod_seen[prefix_mod] = i 
    #     return False
    
    
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     """ Neetcode O(n), O(n) """
    #     #We are basically storing sum%k and storing it in the hashmap and checking it.
    #     #Math logic is that the overall sum will get cancelled out because of modulo

    #     hashmap = {0: -1}
    #     # hashmap[0]=-1
    #     summ=0
    #     for i,j in enumerate(nums):
    #         summ+=j
    #         # if summ%k in hashmap.keys():
    #         if summ%k in hashmap:
    #             if i-hashmap[summ%k]>=2:
    #                 return True
    #             else:
    #                 continue
    #         hashmap[summ%k]=i
    #     return False    
    
    #  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     """ Neetcode O(n), O(n) """
    #     #We are basically storing sum%k and storing it in the hashmap and checking it.
    #     #Math logic is that the overall sum will get cancelled out because of modulo

    #     hashmap = {0: -1}
    #     # hashmap[0]=-1
    #     summ=0
    #     for i,j in enumerate(nums):
    #         summ+=j
    #         # if summ%k in hashmap.keys():
    #         if summ%k in hashmap:
    #             if i-hashmap[summ%k]>=2:
    #                 return True
    #             # else:
    #             #     continue
    #         else:
    #             hashmap[summ%k]=i
    #     return False    
     
    #  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     """ practice; Neetcode O(n), O(n) """
    #     hashmap = {0: -1}
    #     prefix_sum = 0
    #     for i, num in enumerate(nums):
    #         prefix_sum += num
    #         if prefix_sum % k in hashmap:
    #             if i - hashmap[prefix_sum % k] >= 2:
    #                 return True
    #         else:
    #             hashmap[prefix_sum % k] = i
    #     return False
     
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """ practice; Neetcode O(n), O(n) """ 
        hashmap = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num 
            if prefix_sum % k in hashmap:
                if i - hashmap[prefix_sum % k] >= 2:
                    return True
            else:
                hashmap[prefix_sum % k] = i 
        return False
        
# @lc code=end

