#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    # def shipWithinDays(self, weights: List[int], days: int) -> int:
    #     """ my first atempt """
    #     low = max(weights), high = sum(weights)
    #     capacity = high
    #     while low < high:
    #         mid = (low + high) // 2
    #         num_days = sum(weights)/capacity
    #         if num_days < days:
    #             low = capacity + 1
    #         else:
    #             high = capacity + 1
    #     return capacity
    
     def shipWithinDays(self, weights: List[int], days: int) -> int:
        """ cracking faang binary search, O(n log n), O(1) """
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if self.can_ship(mid, weights, days):
                r = mid
            else:
                l = mid + 1
        return r
     
     def can_ship(self, candidate, weights, days):
         cur_weight = 0
         days_taken = 1
         for weight in weights:
             cur_weight += weight
             if cur_weight > candidate:
                 days_taken += 1
                 cur_weight = weight
         return days_taken <= days



# @lc code=end

