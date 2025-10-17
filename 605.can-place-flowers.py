#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    #     """ Approach #1 Single Scan O(n), O(1) """
    #     count = 0
    #     for i in range(len(flowerbed)):
    #         # Check if the current plot is empty.
    #         if flowerbed[i] == 0:
    #             # Check if the left and right plots are empty.
    #             empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
    #             empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
    #             # If both plots are empty, we can plant a flower here.
    #             if empty_left_plot and empty_right_lot:
    #                 flowerbed[i] = 1
    #                 count += 1
                    
    #     return count >= n

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """ Approach #2 Optimized [Accepted] O(n), O(1) """
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
                    
        return count >= n
        
# @lc code=end

