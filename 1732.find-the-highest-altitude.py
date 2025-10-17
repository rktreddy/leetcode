#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    # def largestAltitude(self, gain: List[int]) -> int:
    #     """ Approach: Prefix Sum O(n), O(1) """
    #     current_altitude = 0
    #     # Highest altitude currently is 0.
    #     highest_point = current_altitude
        
    #     for altitude_gain in gain:
    #         # Adding the gain in altitude to the current altitude.
    #         current_altitude += altitude_gain
    #         # Update the highest altitude.
    #         highest_point = max(highest_point, current_altitude)
        
    #     return highest_point
    
    def largestAltitude(self, gain: List[int]) -> int:
        """ practice: Approach: Prefix Sum O(n), O(1) """
        current_altitude = 0
        highest_point = current_altitude
        for altitude_gain in gain:
            current_altitude += altitude_gain
            highest_point = max(highest_point, current_altitude)
        return highest_point
        
# @lc code=end

