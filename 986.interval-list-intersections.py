#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    # def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    #     """ Approach 1: Merge Intervals O(m + n), O(m + n) """
    #     ans = []
    #     i = j = 0

    #     while i < len(firstList) and j < len(secondList):
    #         lo = max(firstList[i][0], secondList[j][0])
    #         hi = min(firstList[i][1], secondList[j][1])

    #         if lo <= hi:
    #             ans.append([lo, hi])

    #         if firstList[i][1] < secondList[j][1]:
    #             i += 1
    #         else:
    #             j += 1

    #     return ans
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """ practice: Approach 1: Merge Intervals O(m + n), O(m + n) """
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])

            if lo <= hi:
                ans.append([lo, hi])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans


# @lc code=end

