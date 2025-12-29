#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     """ 1. Brute Force O(n^2), O(1) """
    #     for i in range(len(nums)):
    #         flag = True
    #         for j in range(len(nums)):
    #             if i != j and nums[i] == nums[j]:
    #                 flag = False
    #                 break
    #         if flag:
    #             return nums[i]
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     """ 2. Hash Set O(n), O(n) """
    #     seen = set()
    #     for num in nums:
    #         if num in seen:
    #             seen.remove(num)
    #         else:
    #             seen.add(num)
    #     return list(seen)[0]
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     """ 3. Sorting O(nlogn), O(1) to O(n) """
    #     nums.sort()
    #     i = 0
    #     while i < len(nums) - 1:
    #         if nums[i] == nums[i + 1]:
    #             i += 2
    #         else:
    #             return nums[i]
    #     return nums[i]

    # def singleNumber(self, nums: List[int]) -> int:
    #     """ 4. Bit Manipulation, O(n),  O(1) """
    #     res = 0
    #     for num in nums:
    #         res = num ^ res
    #     return res
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     """ practice: 4. Bit Manipulation, O(n),  O(1) """
    #     res = 0
    #     for num in nums:
    #         res = num ^ res
    #         # print(f'res: {res}, num: {num}')
    #     return res 
    
    def singleNumber(self, nums: List[int]) -> int:
        """ practice: 4. Bit Manipulation, O(n),  O(1) """
        res = 0
        for num in nums:
            res = res ^ num 
        return res 

# @lc code=end

# res: 2, num: 2
# res: 0, num: 2
# res: 1, num: 1

