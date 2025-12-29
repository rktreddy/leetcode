#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     """ my initial trial"""
        # def findIndex(intervals, newInterval, index):
        #     left, right = 0, len(intervals) - 1
        #     mid = (left + right) // 2
        #     while left < right:
        #         if intervals[mid][index] < newInterval[index]:
        #             left = mid + 1
        #         else:
        #             right = mid
        #     return left
        # start_index = findIndex(intervals, newInterval, 0)
        # end_index = findIndex(intervals, newInterval, 1)
        
        # new_intervals = []
        # for i in range(start_index):
        #     new_intervals.append(intervals[i])

        # """ Approach 1: Linear Search O(N), O(1)"""
        # n = len(intervals)
        # i = 0
        # res = []

        # # Case 1: No overlapping before merging intervals
        # while i < n and intervals[i][1] < newInterval[0]:
        #     res.append(intervals[i])
        #     i += 1

        # # Case 2: Overlapping and merging intervals
        # while i < n and newInterval[1] >= intervals[i][0]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # res.append(newInterval)

        # # Case 3: No overlapping after merging newInterval
        # while i < n:
        #     res.append(intervals[i])
        #     i += 1

        # return res
    
        # """ Approach 2: Binary Search O(N), O(logN_)"""
        # if not intervals:
        #     return [newInterval]
        
        # n = len(intervals)
        # target = newInterval[0]
        # left, right = 0, n - 1

        # while left <= right:
        #     mid = (left + right) // 2
        #     if intervals[mid][0] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # intervals.insert(left, newInterval)

        # res = []
        # for interval in intervals:
        #     if not res or res[-1][1] < interval[0]:
        #         res.append(interval)
        #     else:
        #         res[-1][1] = max(interval[1], res[-1][1])

        # return res
    
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     """ Approach 2: Binary Search O(N), O(logN_)"""
    #     if not intervals:
    #         return [newInterval]
        
    #     target = newInterval[0]
    #     l, r = 0, len(intervals) - 1
        
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if intervals[mid][0] < target:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
        
    #     intervals.insert(l, newInterval)

    #     merged = []
    #     for interval in intervals:
    #         if not merged or merged[-1][1] < interval[0]:
    #             merged.append(interval)
    #         else:
    #             merged[-1][1] = max(merged[-1][1], interval[1])
    #     return merged
    
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     """ practice: Approach 2: Binary Search O(N), O(N) """
    #     if not intervals:
    #         return [newInterval]
    #     target = newInterval[0]
    #     l, r = 0, len(intervals) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if intervals[mid][0] < target:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     intervals.insert(l, newInterval)
    #     merged = []
    #     for interval in intervals:
    #         if not merged or merged[-1][1] < interval[0]:
    #             merged.append(interval)
    #         else:
    #             merged[-1][1] = max(merged[-1][1], interval[1])
    #     return merged
    
    # def insert(self, intervals, newInterval):
    #     res = []
    #     i = 0
    #     n = len(intervals)

    #     # 1. Add all intervals before newInterval
    #     while i < n and intervals[i][1] < newInterval[0]:
    #         res.append(intervals[i])
    #         i += 1

    #     # 2. Merge overlapping intervals
    #     while i < n and intervals[i][0] <= newInterval[1]:
    #         newInterval[0] = min(newInterval[0], intervals[i][0])
    #         newInterval[1] = max(newInterval[1], intervals[i][1])
    #         i += 1

    #     res.append(newInterval)

    #     # 3. Add remaining intervals
    #     while i < n:
    #         res.append(intervals[i])
    #         i += 1

    #     return res
    
    def insert(self, intervals, newInterval):
        """ practuce: """
        res = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


# @lc code=end

# """ chatgpt: one-pass approach (standard interview answer): O(N), O(N) """
