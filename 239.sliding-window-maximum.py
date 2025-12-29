#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
# class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     dq = deque()
    #     res = []
    #     for i in range(k):
    #         while dq and nums[i] >= nums[dq[-1]]:
    #             dq.pop()
    #         dq.append(i)

    #     res.append(nums[dq[0]])

    #     for i in range(k, len(nums)):
    #         if dq and dq[0] == i - k:
    #             dq.popleft()
    #         while dq and nums[i] >= nums[dq[-1]]:
    #             dq.pop()

    #         dq.append(i)
    #         res.append(nums[dq[0]])

    #     return res
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     """ Brute Force O(n * k), O(1) extra and O(n - k + 1). for output"""
    #     output = []

    #     for i in range(len(nums) - k + 1):
    #         maxi = nums[i]
    #         for j in range(i, i + k):
    #             maxi = max(maxi, nums[j])
    #         output.append(maxi)

    #     return output
    
# class SegmentTree:
#     def __init__(self, N, A):
#         self.n = N
#         while (self.n & (self.n - 1)) != 0:
#             self.n += 1
#         self.build(N, A)

#     def build(self, N, A):
#         self.tree = [float('-inf')] * (2 * self.n)
#         for i in range(N):
#             self.tree[self.n + i] = A[i]
#         for i in range(self.n - 1, 0, -1):
#             self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

#     def query(self, l, r):
#         res = float('-inf')
#         l += self.n
#         r += self.n + 1
#         while l < r:
#             if l & 1:
#                 res = max(res, self.tree[l])
#                 l += 1
#             if r & 1:
#                 r -= 1
#                 res = max(res, self.tree[r])
#             l >>= 1
#             r >>= 1
#         return res


# class Solution:
#     """ Segment Tree O(nlogn), O(n) """
#     def maxSlidingWindow(self, nums, k):
#         n = len(nums)
#         segTree = SegmentTree(n, nums)
#         output = []
#         for i in range(n - k + 1):
#             output.append(segTree.query(i, i + k - 1))
#         return output
        
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         """ heap O(nlogn), O(n) """
#         heap = []
#         output = []
#         for i in range(len(nums)):
#             heapq.heappush(heap, (-nums[i], i))
#             if i >= k - 1:
#                 while heap[0][1] <= i - k:
#                     heapq.heappop(heap)
#                 output.append(-heap[0][0])
#         return output
    
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         """ dynamic programing O(n), O(n) """
#         n = len(nums)
#         leftMax = [0] * n
#         rightMax = [0] * n

#         leftMax[0] = nums[0]
#         rightMax[n - 1] = nums[n - 1]

#         for i in range(1, n):
#             if i % k == 0:
#                 leftMax[i] = nums[i]
#             else:
#                 leftMax[i] = max(leftMax[i - 1], nums[i])

#             if (n - 1 - i) % k == 0:
#                 rightMax[n - 1 - i] = nums[n - 1 - i]
#             else:
#                 rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - 1 - i])

#         output = [0] * (n - k + 1)

#         for i in range(n - k + 1):
#             output[i] = max(leftMax[i + k - 1], rightMax[i])

#         return output
    
from collections import deque
class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     """ deque O(n), O(n) """
    #     output = []
    #     q = deque()  # index
    #     l = r = 0

    #     while r < len(nums):
    #         while q and nums[q[-1]] < nums[r]:
    #             q.pop()
    #         q.append(r)

    #         if l > q[0]:
    #             q.popleft()

    #         if (r + 1) >= k:
    #             output.append(nums[q[0]])
    #             l += 1
    #         r += 1

    #     return output
    
     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ practice: deque O(n), O(n) """
        output = []
        q = deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

    
# @lc code=end

