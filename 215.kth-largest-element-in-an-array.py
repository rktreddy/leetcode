#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    # # O(nlogn) time
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return sorted(nums, reverse=True)[k-1]
    
    # # O(nk) time, bubble sort idea, TLE
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     for i in range(k):
    #         for j in range(len(nums)-i-1):
    #             if nums[j] > nums[j+1]:
    #                 # exchange elements, time consuming
    #                 nums[j], nums[j+1] = nums[j+1], nums[j]
    #     return nums[len(nums)-k]

    # # O(nk) time, selection sort idea
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     for i in range(len(nums), len(nums)-k, -1):
    #         tmp = 0
    #         for j in range(i):
    #             if nums[j] > nums[tmp]:
    #                 tmp = j
    #         nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    #     return nums[len(nums)-k]

    # # O(k+(n-k)lgk) time, min-heap
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heap = []
    #     for num in nums:
    #         heapq.heappush(heap, num)
    #     for _ in range(len(nums)-k):
    #         heapq.heappop(heap)
    #     return heapq.heappop(heap)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heap = nums[:k]
    #     heapify(heap)
    #     for n in nums[k:]:
    #         heappushpop(heap, n)
    #     return heap[0]

    # # O(k+(n-k)lgk) time, min-heap        
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #         return heapq.nlargest(k, nums)[-1]

    # # O(n) time, quick selection # taking very long
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # convert the kth largest to smallest
    #     return self.findKthLargest(nums, len(nums)+1-k)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     if nums:
    #         pos = self.partition(nums, 0, len(nums)-1)
    #         if k > pos+1:
    #             return self. findKthLargest(nums[pos+1:], k-pos-1)
    #         elif k < pos+1:
    #             return self.findKthLargest(nums[:pos], k)
    #         else:
    #             return nums[pos]
    
    # # choose the right-most element as pivot   
    # def partition(self, nums, l, r):
    #     low = l
    #     while l < r:
    #         if nums[l] < nums[r]:
    #             nums[l], nums[low] = nums[low], nums[l]
    #             low += 1
    #         l += 1
    #     nums[low], nums[r] = nums[r], nums[low]
    #     return low

    ## Leetcode solutions
    # # Approach 1: Sort O(nlogn), O(logn) or O(n)
    # def findKthLargest(self, nums, k):
    #     nums.sort(reverse=True)
    #     return nums[k - 1]

    # # Approach 2: Min-Heap O(nlogk), o(k)
    # def findKthLargest(self, nums, k):
    #     heap = []
    #     for num in nums:
    #         heapq.heappush(heap, num)
    #         if len(heap) > k:
    #             heapq.heappop(heap)
        
    #     return heap[0]

    # # Approach 2: Min-Heap O(nlogk), o(k)
    # def findKthLargest(self, nums, k):
    #     """ practice """
    #     heap = []
    #     for num in nums:
    #         heapq.heappush(heap, num)
    #         if len(heap) > k:
    #             heapq.heappop(heap)
    #     return heap[0]
    
    def findKthLargest(self, nums, k):
        """ practice """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
    
    # # Approach 3: Quickselect O(n) to O(n^2), O(n)
    # def findKthLargest(self, nums, k):
    #     def quick_select(nums, k):
    #         pivot = random.choice(nums)
    #         left, mid, right = [], [], []

    #         for num in nums:
    #             if num > pivot:
    #                 left.append(num)
    #             elif num < pivot:
    #                 right.append(num)
    #             else:
    #                 mid.append(num)
            
    #         if k <= len(left):
    #             return quick_select(left, k)
            
    #         if len(left) + len(mid) < k:
    #             return quick_select(right, k - len(left) - len(mid))
            
    #         return pivot
        
    #     return quick_select(nums, k)

    # # Approach 4: Counting Sort O(n + m), O(m)
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     min_value = min(nums)
    #     max_value = max(nums)
    #     count = [0] * (max_value - min_value + 1)

    #     for num in nums:
    #         count[num - min_value] += 1
        
    #     remain = k
    #     for num in range(len(count) -1, -1, -1):
    #         remain -= count[num]
    #         if remain <= 0:
    #             return num + min_value

    #     return -1

# @lc code=end

