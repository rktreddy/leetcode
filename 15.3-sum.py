#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach 1: Two Pointers O(n^2), O(log n) to O(n) """
    #     res = []
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if nums[i] > 0:
    #             break
    #         if i == 0 or nums[i - 1] != nums[i]:
    #             self.twoSumII(nums, i, res)
    #     return res

    # def twoSumII(self, nums, i, res):
    #     lo, hi = i + 1, len(nums) - 1
    #     while lo < hi:
    #         three_sum = nums[i] + nums[lo] + nums[hi]
    #         if three_sum < 0:
    #             lo += 1
    #         elif three_sum > 0:
    #             hi -= 1
    #         else:
    #             res.append([nums[i], nums[lo], nums[hi]])
    #             lo += 1
    #             hi -= 1
    #             while lo < hi and nums[lo] == nums[lo - 1]:
    #                 lo += 1

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach 2: Hashset O(n^2), O(n)  """
    #     res = []
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if nums[i] > 0:
    #             break
    #         if i == 0 or nums[i - 1] != nums[i]:
    #             self.twoSum(nums, i, res)

    #     return res
        
    # def twoSum(self, nums, i, res):
    #     seen = set()
    #     j = i + 1
    #     while j < len(nums):
    #         complement = -nums[i] - nums[j]
    #         if complement in seen:
    #             res.append([nums[i], nums[j], complement])
    #             while j + 1 < len(nums) and nums[j] == nums[j + 1]:
    #                 j += 1
    #         seen.add(nums[j])
    #         j += 1

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach 3: "No-Sort" O(n^2), O(n) - slower than previous"""
    #     res, dups = set(), set()
    #     seen = {}

    #     for i, val1 in enumerate(nums):
    #         if val1 not in dups:
    #             dups.add(val1)
    #             for j, val2 in enumerate(nums[i + 1:]):
    #                 complement = - val1 - val2
    #                 if complement in seen and seen[complement] == i:
    #                     res.add(tuple(sorted((val1, val2, complement))))
    #                 seen[val2] = i
    #     return res

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     """ Neetcode solution O(n^2), O(1)  """
    #     res = []
    #     nums.sort()

    #     for i, a in enumerate(nums):
    #         # Skip positive integers
    #         if a > 0:
    #             break

    #         if i > 0 and a == nums[i - 1]:
    #             continue

    #         l, r = i + 1, len(nums) - 1
    #         while l < r:
    #             threeSum = a + nums[l] + nums[r]
    #             if threeSum > 0:
    #                 r -= 1
    #             elif threeSum < 0:
    #                 l += 1
    #             else:
    #                 res.append([a, nums[l], nums[r]])
    #                 l += 1
    #                 r -= 1
    #                 while nums[l] == nums[l - 1] and l < r:
    #                     l += 1
                        
    #     return res
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ practice: Neetcode solution O(n^2), O(1)  """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

        
# @lc code=end

