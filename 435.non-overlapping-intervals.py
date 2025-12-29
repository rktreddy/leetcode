#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     """ Approach: Greedy O(nlogn), o(logn) to o(n) """
    #     intervals.sort(key=lambda x: x[1])
    #     ans = 0
    #     k = -inf

    #     for x, y in intervals:
    #         if x >= k:
    #             k = y
    #         else:
    #             ans += 1

    #     return ans
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """ practice: Approach: Greedy O(nlogn), o(logn) to o(n) """
        intervals.sort(key=lambda x: x[1])
        ans = 0
        k = -inf
        for x, y in intervals:
            if x >= k:
                k = y
            else:    
                ans += 1
        return ans
        
# @lc code=end

