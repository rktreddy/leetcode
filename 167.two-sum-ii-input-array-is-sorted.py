#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     """ Approach 1: Two Pointers O(n), O(1) """
    #     low, high = 0, len(numbers) - 1

    #     while low < high:
    #         two_sum = numbers[low] + numbers[high]

    #         if two_sum == target:
    #             return [low + 1, high + 1]
    #         elif two_sum < target:
    #             low += 1
    #         else: 
    #             high -= 1
    #     return [-1, -1] 
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ practice: Approach 1: Two Pointers O(n), O(1) """
        low, high = 0, len(numbers) - 1
        while low < high:
            two_sum = numbers[low] + numbers[high]
            if two_sum == target:
                return [low + 1, high + 1]
            elif two_sum < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]

# @lc code=end

