#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     """ Approach 1: Left and Right product lists O(N), O(N) """
    #     length = len(nums)

    #     L, R, answer = [0] * length, [0] * length, [0] * length

    #     L[0] = 1
    #     for i in range(1, length):
    #         L[i] = nums[i - 1] * L[i - 1]

    #     R[length - 1] = 1
    #     for i in reversed(range(length - 1)):
    #         R[i] = nums[i + 1] * R[i + 1]

    #     for i in range(length):
    #         answer[i] = L[i] * R[i]

    #     return answer

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     """ Approach 2: O(1) space approach O(N), (1)"""
    #     length = len(nums)

    #     answer = [0] * length

    #     answer[0] = 1
    #     for i in range(1, length):
    #         answer[i] = nums[i - 1] * answer[i - 1]

    #     R = 1
    #     for i in reversed(range(length)):
    #         answer[i] = answer[i] * R
    #         R *= nums[i]
        
    #     return answer
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ practice: Approach 2: O(1) space approach O(N), O(1)"""
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]

        right = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


# @lc code=end

# nums = [1, 2, 3, 4]
# length = 4
# answer = [0, 0, 0, 0]
# answer = [1, 1, 2, 6]
# answer = [24, 12, 8, 6]
# R = [24, 24, 12, 4]

