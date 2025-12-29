#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        heap_dict = collections.defaultdict(int)

        res = []
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        if k % 2 == 1:
            median = -max_heap[0]
            res.append(median)
        else:
            median = (-max_heap[0] + min_heap[0]) / 2
            res.append(median)

        for i in range(k, len(nums)):
            prev_num = nums[i - k]
            heap_dict[prev_num] += 1

            balance = -1 if prev_num <= median else 1
            if nums[i] <= median:
                balance += 1
                heapq.heappush(max_heap, -nums[i])
            else:
                balance -= 1
                heapq.heappush(min_heap, nums[i])

            if balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            elif balance > 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heapq.heappop(max_heap)

            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heapq.heappop(min_heap)

            if k % 2 == 1:
                median = -max_heap[0]
                res.append(median)
            else:
                median = (-max_heap[0] + min_heap[0]) / 2
                res.append(median)

        return res
    
    # def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    #     """ chatgpt solution O(n log n), O(k) """
    #     import heapq
    #     from collections import defaultdict

    #     max_heap = []  # lower half (negative)
    #     min_heap = []  # upper half
    #     delayed = defaultdict(int)

    #     def prune(heap):
    #         while heap:
    #             num = -heap[0] if heap is max_heap else heap[0]
    #             if delayed[num] > 0:
    #                 delayed[num] -= 1
    #                 heapq.heappop(heap)
    #             else:
    #                 break

    #     def rebalance():
    #         if len(max_heap) > len(min_heap) + 1:
    #             heapq.heappush(min_heap, -heapq.heappop(max_heap))
    #         elif len(max_heap) < len(min_heap):
    #             heapq.heappush(max_heap, -heapq.heappop(min_heap))

    #     res = []

    #     # Initial window
    #     for i in range(k):
    #         heapq.heappush(max_heap, -nums[i])
    #         heapq.heappush(min_heap, -heapq.heappop(max_heap))
    #         if len(min_heap) > len(max_heap):
    #             heapq.heappush(max_heap, -heapq.heappop(min_heap))

    #     for i in range(k, len(nums) + 1):
    #         # Get median
    #         if k % 2:
    #             res.append(float(-max_heap[0]))
    #         else:
    #             res.append((-max_heap[0] + min_heap[0]) / 2)

    #         if i == len(nums):
    #             break

    #         out_num = nums[i - k]
    #         in_num = nums[i]

    #         delayed[out_num] += 1

    #         if out_num <= -max_heap[0]:
    #             balance = -1
    #         else:
    #             balance = 1

    #         if in_num <= -max_heap[0]:
    #             heapq.heappush(max_heap, -in_num)
    #             balance += 1
    #         else:
    #             heapq.heappush(min_heap, in_num)
    #             balance -= 1

    #         if balance < 0:
    #             heapq.heappush(max_heap, -heapq.heappop(min_heap))
    #         elif balance > 0:
    #             heapq.heappush(min_heap, -heapq.heappop(max_heap))

    #         prune(max_heap)
    #         prune(min_heap)

    #     return res


        
# @lc code=end

# """ cracking faang: two heap: T: O(n log k), S: O(k) """
