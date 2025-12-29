#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:

    # def __init__(self, w: List[int]):
    #     """
    #     Approach 1: Prefix Sums with Linear Search T O(N), O(N), S: O(N), O(N)
    #     :type w: List[int]
    #     """
    #     self.prefix_sums = []
    #     prefix_sum = 0
    #     for weight in w:
    #         prefix_sum += weight
    #         self.prefix_sums.append(prefix_sum)
    #     self.total_sum = prefix_sum

    # def pickIndex(self) -> int:
    #     """
    #     
    #     :rtype: int
    #     """
    #     target = self.total_sum * random.random()
    #     # run a linear search to find the target zone
    #     for i, prefix_sum in enumerate(self.prefix_sums):
    #         if target < prefix_sum:
    #             return i
        
    # def __init__(self, w: List[int]):
    #     """
    #     Approach 2: Prefix Sums with Binary Search Time O(N), O(logN), Space O(N), O(1)
    #     :type w: List[int]
    #     """
    #     self.prefix_sums = []
    #     prefix_sum = 0
    #     for weight in w:
    #         prefix_sum += weight
    #         self.prefix_sums.append(prefix_sum)
    #     self.total_sum = prefix_sum

    # def pickIndex(self) -> int:
    #     """
    #     :rtype: int
    #     """
    #     target = self.total_sum * random.random()
    #     # run a binary search to find the target zone
    #     low, high = 0, len(self.prefix_sums)
    #     while low < high:
    #         mid = low + (high - low) // 2
    #         if target > self.prefix_sums[mid]:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return low


    # ## practice here

    # def __init__(self, w: List[int]):
    #     self.prefix_sums = []
    #     prefix_sum = 0
    #     for weight in w:
    #         prefix_sum += weight
    #         self.prefix_sums.append(prefix_sum)
    #     self.total_sum = prefix_sum

    # def pickIndex(self) -> int:
    #     target = self.total_sum * random.random()
    #     low, high = 0, len(self.prefix_sums)
    #     while low < high:
    #         mid = (low + high) // 2
    #         if self.prefix_sums[mid] < target:
    #             low = mid + 1
    #         else:
    #             high = mid 
    #     return low 
        
    # def __init__(self, w):
    #     """ Approach 2: Prefix Sums with Binary Search O(n), O(n) """
    #     self.prefix_sums = []
    #     prefix_sum = 0
    #     for weight in w:
    #         prefix_sum += weight
    #         self.prefix_sums.append(prefix_sum)
    #     self.total_sum = prefix_sum

    # def pickIndex(self):
    #     """ Approach 2: Prefix Sums with Binary Search O(logn), O(1) """
    #     target = self.total_sum * random.random()
    #     low, high = 0, len(self.prefix_sums)
    #     while low < high:
    #         mid = (low + high) // 2
    #         if self.prefix_sums[mid] < target:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return low

    def __init__(self, w):
        self.prefix_sums = []
        prefix_sum = 0
        for wt in w:
            prefix_sum += wt
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        target = self.total_sum * random.random()
        l, r = 0, len(self.prefix_sums)
        while l < r:
            mid = (l + r) // 2
            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

        

    # ## practice here

    
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

