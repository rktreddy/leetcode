#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start
class Solution:
    # def angleClock(self, hour: int, minutes: int) -> float:
    #     """ my first attempt O(1), O(1) """
    #     return min(abs(hour/12 * 360 + 1/12 * 360 * minutes/60 - minutes/60 * 360), 
    #                360 - abs(hour/12 * 360 + 1/12 * 360 * minutes/60 - minutes/60 * 360))
    
    def angleClock(self, hour: int, minutes: int) -> float:
        """ Leet code: Math O(1), O(1) """
        one_min_angle = 6
        one_hour_angle = 30
        
        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle
        
        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)
        
# @lc code=end

