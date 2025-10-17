#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    # def findMaxLength(self, nums: List[int]) -> int:
    #     cum_sum = []
    #     tsum = nums[0]
    #     cum_sum.append(tsum)
    #     for i in range(1, len(nums)):
    #         tsum += nums[i]
    #         cum_sum.append(tsum)

    #     max_len = 0
    #     sub_len = 0
    #     left, right = 0, 0
    #     while left < len(nums) and right < len(nums)
    #         while cum_sum[right] - cum_sum[left] + nums[left] in [0, 1]:
    #             right += 1
    #             sub_len += 1
    #             max_len = max(max_len, sub_len)
    #         left, right = 0, 0


    def findMaxLength(self, nums: List[int]) -> int:
        """ Neetcode solution O(N) """
        zero, one = 0, 0
        res = 0
        
        diff_index = {}
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in diff_index:
                diff_index[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = diff_index[one - zero]
                res = max(res, i - idx)

        return res 

        
# @lc code=end

