#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     """ Approach 1: Sort with Custom Comparator O(N Log N), O(Log N) to O(N)"""

    #     points.sort(key = self.squared_distance)
    #     return points[:k]
    
    # def squared_distance(self, point):
    #     return point[0] ** 2 + point[1] ** 2

    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     """ Approach 2: Max Heap or Max Priority Queue O(N Log k), O(k)"""
    #     # Since heap is sorted in increasing order,
    #     # negate the distance to simulate max heap
    #     # and fill the heap with the first k elements of points
    #     heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
    #     heapq.heapify(heap)
    #     for i in range(k, len(points)):
    #         dist = -self.squared_distance(points[i])
    #         if dist > heap[0][0]:
    #             # If this point is closer than the kth farthest,
    #             # discard the farthest point and add this one
    #             heapq.heappushpop(heap, (dist, i))
        
    #     # Return all points stored in the max heap
    #     return [points[i] for (_, i) in heap]
    
    # def squared_distance(self, point):
    #     return point[0] ** 2 + point[1] ** 2
    
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     """ Approach 3: Binary Search O(N), O(N) """
    #     # Precompute the Euclidean distance for each point
    #     distances = [self.euclidean_distance(point) for point in points]
    #     # Create a reference list of point indices
    #     remaining = [i for i in range(len(points))]
    #     # Define the initial binary search range
    #     low, high = 0, max(distances)
        
    #     # Perform a binary search of the distances
    #     # to find the k closest points
    #     closest = []
    #     while k:
    #         mid = (low + high) / 2
    #         closer, farther = self.split_distances(remaining, distances, mid)
    #         if len(closer) > k:
    #             # If more than k points are in the closer distances
    #             # then discard the farther points and continue
    #             remaining = closer
    #             high = mid
    #         else:
    #             # Add the closer points to the answer array and keep
    #             # searching the farther distances for the remaining points
    #             k -= len(closer)
    #             closest.extend(closer)
    #             remaining = farther
    #             low = mid
                
    #     # Return the k closest points using the reference indices
    #     return [points[i] for i in closest]

    # def split_distances(self, remaining: List[int], distances: List[float],
    #                     mid: int) -> List[List[int]]:
    #     """Split the distances around the midpoint
    #     and return them in separate lists."""
    #     closer, farther = [], []
    #     for index in remaining:
    #         if distances[index] <= mid:
    #             closer.append(index)
    #         else:
    #             farther.append(index)
    #     return [closer, farther]

    # def euclidean_distance(self, point: List[int]) -> float:
    #     """Calculate and return the squared Euclidean distance."""
    #     return point[0] ** 2 + point[1] ** 2
        
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     """ Approach 4: QuickSelect """
    #     return self.quick_select(points, k)
    
    # def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     """Perform the QuickSelect algorithm on the list"""
    #     left, right = 0, len(points) - 1
    #     pivot_index = len(points)
    #     while pivot_index != k:
    #         # Repeatedly partition the list
    #         # while narrowing in on the kth element
    #         pivot_index = self.partition(points, left, right)
    #         if pivot_index < k:
    #             left = pivot_index
    #         else:
    #             right = pivot_index - 1
        
    #     # Return the first k elements of the partially sorted list
    #     return points[:k]
    
    # def partition(self, points: List[List[int]], left: int, right: int) -> int:
    #     """Partition the list around the pivot value"""
    #     pivot = self.choose_pivot(points, left, right)
    #     pivot_dist = self.squared_distance(pivot)
    #     while left < right:
    #         # Iterate through the range and swap elements to make sure
    #         # that all points closer than the pivot are to the left
    #         if self.squared_distance(points[left]) >= pivot_dist:
    #             points[left], points[right] = points[right], points[left]
    #             right -= 1
    #         else:
    #             left += 1
        
    #     # Ensure the left pointer is just past the end of
    #     # the left range then return it as the new pivotIndex
    #     if self.squared_distance(points[left]) < pivot_dist:
    #         left += 1
    #     return left
    
    # def choose_pivot(self, points: List[List[int]], left: int, right: int) -> List[int]:
    #     """Choose a pivot element of the list"""
    #     return points[left + (right - left) // 2]
    
    # def squared_distance(self, point: List[int]) -> int:
    #     """Calculate and return the squared Euclidean distance."""
    #     return point[0] ** 2 + point[1] ** 2

    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     """ Solution 3: Binary Search O(n log M), o(n) """
    #     dist = [x * x + y * y for x, y in points]
    #     l, r = 0, max(dist)
    #     while l < r:
	#   		# mid = (l + r) >> 1
    #         mid = (l + r) // 2
    #         cnt = sum(d <= mid for d in dist)
    #         if cnt >= k:
    #             r = mid
    #         else:
    #             l = mid + 1
    #     return [points[i] for i, d in enumerate(dist) if d <= l]

    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     """ Solution 3: Binary Search O(n log M), o(n) """
    #     dist = [x * x + y *y for x, y in points]
    #     l, r = 0, max(dist)
    #     while l < r:
    #         mid = (l + r) // 2
    #         count = sum(d <= mid for d in dist)
    #         if count >= k:
    #             r = mid
    #         else:
    #             l = mid + 1

    #     return [points[i] for i, d in enumerate(dist) if d <= l]
    
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     minHeap = []
    #     for x, y in points:
    #         dist = (x ** 2) + (y ** 2)
    #         minHeap.append((dist, x, y))
        
    #     heapq.heapify(minHeap)
    #     res = []
    #     for _ in range(k):
    #         _, x, y = heapq.heappop(minHeap)
    #         res.append((x, y))
    #     return res
    
	# def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
	# 	""" Min Heap P(nlogk), O(k) """
	# 	# minHeap = []
	# 	minHeap = [(x * x + y * y, x, y) for x, y in points]
	# 	heapq.heapify(minHeap)
	# 	res = []
	# 	for _ in range(k):
	# 		_, x, y = heapq.heappop(minHeap)
	# 		res.append((x, y))
	# 	return res 

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ practice: Min Heap P(nlogk), O(k) """
        minHeap = [(x * x + y * y, x, y) for x, y in points]
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res

    
        
# @lc code=end

