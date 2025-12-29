#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
# from heapq import *
# class MedianFinder:
#     def __init__(self):
#         self.small = []  # the smaller half of the list, max heap (invert min-heap)
#         self.large = []  # the larger half of the list, min heap

#     def addNum(self, num):
#         if len(self.small) == len(self.large):
#             heappush(self.large, -heappushpop(self.small, -num))
#         else:
#             heappush(self.small, -heappushpop(self.large, num))

#     def findMedian(self):
#         if len(self.small) == len(self.large):
#             return float(self.large[0] - self.small[0]) / 2.0
#         else:
#             return float(self.large[0])


class MedianFinder:
    """ 
    cracking faang: sorting - not efficient O(n log n) + o(1)
    for sorted array: insertion - O(log n) + O(n)
    optimal: two heaps solution O(log n), O(n)
    """

    def __init__(self):
        self.small = [] # smaller half (use max heap)
        self.large = [] # larger half (use mi heap)

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.
        else:
            return float(self.large[0])
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

