#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         """ Approach 1: Heap O(N log k), O(N+k)"""
#         # O(1) time 
#         if k == len(nums):
#             return nums
        
#         # 1. Build hash map: character and how often it appears
#         # O(N) time
#         count = Counter(nums)   
#         # 2-3. Build heap of top k frequent elements and
#         # convert it into an output array
#         # O(N log k) time
#         return heapq.nlargest(k, count.keys(), key=count.get) 
    
from collections import Counter
class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """ Approach 2: Quickselect (Hoare's selection algorithm) O(N), O(N) """
    #     count = Counter(nums)
    #     unique = list(count.keys())
        
    #     def partition(left, right, pivot_index) -> int:
    #         pivot_frequency = count[unique[pivot_index]]
    #         # 1. Move the pivot to end
    #         unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
    #         # 2. Move all less frequent elements to the left
    #         store_index = left
    #         for i in range(left, right):
    #             if count[unique[i]] < pivot_frequency:
    #                 unique[store_index], unique[i] = unique[i], unique[store_index]
    #                 store_index += 1

    #         # 3. Move the pivot to its final place
    #         unique[right], unique[store_index] = unique[store_index], unique[right]  
            
    #         return store_index
        
    #     def quickselect(left, right, k_smallest) -> None:
    #         """
    #         Sort a list within left..right till kth less frequent element
    #         takes its place. 
    #         """
    #         # base case: the list contains only one element
    #         if left == right: 
    #             return
            
    #         # Select a random pivot_index
    #         pivot_index = random.randint(left, right)     
                            
    #         # Find the pivot position in a sorted list   
    #         pivot_index = partition(left, right, pivot_index)
            
    #         # If the pivot is in its final sorted position
    #         if k_smallest == pivot_index:
    #              return 
    #         # go left
    #         elif k_smallest < pivot_index:
    #             quickselect(left, pivot_index - 1, k_smallest)
    #         # go right
    #         else:
    #             quickselect(pivot_index + 1, right, k_smallest)
         
    #     n = len(unique) 
    #     # kth top frequent element is (n - k)th less frequent.
    #     # Do a partial sort: from less frequent to the most frequent, till
    #     # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
    #     # All elements on the left are less frequent.
    #     # All the elements on the right are more frequent.  
    #     quickselect(0, n - 1, n - k)
    #     # Return top k frequent elements
    #     return unique[n - k:]
        
    # def topKFrequent(self, nums, k):
    #     """ top voted: Python O(n) solution without sort, without heap,
    #       without quickselect
    #     """
    #     hs = {}
    #     frq = {}
        
    #     for i, num in enumerate(nums):
    #         if num not in hs:
    #             hs[num] = 1
    #         else:
    #             hs[num] += 1

    #     for z, v in hs.items():
    #         if v not in frq:
    #             frq[v] = [z]
    #         else:
    #             frq[v].append(z)
        
    #     arr = []
        
    #     for x in range(len(nums), 0, -1):
    #         if x in frq:
                
    #             for i in frq[x]:
    #                 arr.append(i)

    #     return [arr[x] for x in range(0, k)]
    
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """ neetcode o(n) bucket sort"""
    #     count = {}
    #     freq = [[] for i in range(len(nums) + 1)]

    #     for n in nums:
    #         count[n] = 1 + count.get(n, 0)
    #     for n, c in count.items():
    #         freq[c].append(n)

    #     res = []
    #     for i in range(len(freq) - 1, 0, -1):
    #         for n in freq[i]:
    #             res.append(n)
    #             if len(res) == k:
    #                 return res
                

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """ practice: neetcode o(n) bucket sort """
    #     count = {}
    #     freq = [[] for _ in range(len(nums) + 1)]
    #     for n in nums:
    #         count[n] = 1 + count.get(n, 0)
    #     for n, c in count.items():
    #         freq[c].append(n)
    #     res = []
    #     for i in range(len(freq) - 1, 0, -1):
    #         for n in freq[i]:
    #             res.append(n)
    #             if len(res) == k:
    #                 return res
                
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ practice: neetcode o(n) bucket sort """
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

                
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """ Approach 1: Heap O(N log k), O(N+k) """
    #     if k == len(nums):
    #         return nums
        
    #     count = Counter(nums)   
    #     return heapq.nlargest(k, count.keys(), key=count.get)

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """ Approach 1: Min-Heap O(N log k), O(N+k) """
    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)

    #     heap = []
    #     for num in count.keys():
    #         heapq.heappush(heap, (count[num], num))
    #         if len(heap) > k:
    #             heapq.heappop(heap)

    #     res = []
    #     for i in range(k):
    #         res.append(heapq.heappop(heap)[1])
    #     return res
        
# @lc code=end

