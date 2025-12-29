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
        i = j = 0
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


    
    # def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    #     """ pcracking faang: Merge Intervals O(m + n), O(m + n) """
    #     if not firstList or not secondList:
    #         return []
    #     p1 = p2 = 0
    #     res = []
    #     while p1 < len(firstList) and p2 < len(secondList):
    #         start1, end1 = firstList[p1]
    #         start2, end2 = secondList[p2]
    #         if start1 > end2:
    #             p2 += 1
    #         elif start2 > end1:
    #             p1 += 1
    #         else:
    #             res.append([max(start1, start2), min(end1, end2)])
    #             if end1 > end2:
    #                 p2 += 1
    #             else:
    #                 p1 += 1

    #     return res
    

# @lc code=end

