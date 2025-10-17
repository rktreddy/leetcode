#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """ Approach 1: Brute Force O(m*n), O(1) """
    #     res = [-1] * len(nums1)
    #     for i, num1 in enumerate(nums1):
    #         found = False
    #         for j, num2 in enumerate(nums2):
    #             if found and num2 > num1:
    #                 res[i] = num2
    #                 break

    #             if num2 == num1:
    #                 found = True

    #     return res
    
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """ Approach 2: Better Brute Force O(m*n), O(n) """
    #     res = [-1] * len(nums1)
    #     for i, num1 in enumerate(nums1):
    #         found = False
    #         for j, num2 in enumerate(nums2):
    #             if found and num2 > num1:
    #                 res[i] = num2
    #                 break

    #             if num2 == num1:
    #                 found = True

    #     return res

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ Approach 3: Using Stack O(n), O(n) """
        stack = []
        hashmap = {}

        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)

        while stack:
            hashmap[stack.pop()] = -1
        
        return [hashmap.get(i, -1) for i in nums1]
        
# @lc code=end

