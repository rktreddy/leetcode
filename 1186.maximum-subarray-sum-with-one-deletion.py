#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#

# @lc code=start
class Solution:
    # def maximumSum(self, arr: List[int]) -> int:
    #     """ cracking faang: O(N), O(1) """
    #     sum_with_skip = sum_no_skip = res = arr[0]
    #     for num in arr[1:]:
    #         if sum_with_skip < 0:
    #             sum_with_skip = 0

    #         if num >= 0:
    #             sum_with_skip += num
    #         else:
    #             sum_with_skip = max(sum_with_skip + num, sum_no_skip)

    #         if sum_no_skip < 0:
    #             sum_no_skip = 0

    #         sum_no_skip += num

    #         res = max(res, sum_no_skip, sum_with_skip)

    #     return res
    
    def maximumSum(self, arr: List[int]) -> int:
        """ practice: cracking faang: O(N), O(1) """
        sum_with_skip = sum_no_skip = res = arr[0]
        for num in arr[1:]:
            if sum_with_skip < 0:
                sum_with_skip = 0

            if num >= 0:
                sum_with_skip += num
            else:
                sum_with_skip = max(sum_with_skip + num, sum_no_skip)
            
            if sum_no_skip < 0:
                sum_no_skip = 0
            
            sum_no_skip += num

            res = max(res, sum_no_skip, sum_with_skip)
        
        return res


# @lc code=end

