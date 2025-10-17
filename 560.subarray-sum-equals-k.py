#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import Counter
class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     """ Approach 4: Using Hashmap O(n), O(n) """
    #     count = 0
    #     sums = 0
    #     # d = dict()
    #     d = {}
    #     d[0] = 1

    #     for i in range(len(nums)):
    #         sums += nums[i]
    #         count += d.get(sums-k, 0)
    #         d[sums] = d.get(sums, 0) + 1

    #     return count
    
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     """ practice: Approach 4: Using Hashmap O(n), O(n) """
    #     count = 0
    #     array_sum = 0
    #     hashmap = {}
    #     hashmap[0] = 1

    #     for num in nums:
    #         array_sum += num
    #         count += hashmap.get(array_sum - k, 0)
    #         hashmap[array_sum] = hashmap.get(array_sum, 0) + 1
    #     return count
    

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     """ Algomonster code O(n), O(n)"""
    #     # Initialize a counter to keep track of the cumulative sums encountered
    #     cumulative_sum_counter = Counter({0: 1})
      
    #     # 'count_subarrays' will store the total count of subarrays that sum up to 'k'
    #     count_subarrays = 0
      
    #     # 'cumulative_sum' holds the sum of numbers seen so far
    #     cumulative_sum = 0
      
    #     # Iterate through the list of numbers
    #     for num in nums:
    #         # Update the cumulative sum
    #         cumulative_sum += num
          
    #         # If there is a previous cumulative sum such that current_sum - k
    #         # is equal to that previous sum, then a subarray ending at the current
    #         # position would sum to 'k'
    #         count_subarrays += cumulative_sum_counter[cumulative_sum - k]
          
    #         # Increase the count of the current cumulative sum by 1 in the counter
    #         cumulative_sum_counter[cumulative_sum] += 1
      
    #     # Return the total number of subarrays that sum up to 'k'
    #     return count_subarrays
    
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     """ practice: Algomonster code O(n), O(n) """
    #     cum_sum_count = Counter({0: 1})
    #     count_subarrays = 0
    #     cum_sum = 0
    #     for num in nums:
    #         cum_sum += num
    #         count_subarrays += cum_sum_count.get(cum_sum - k, 0)
    #         cum_sum_count[cum_sum] += 1
    #     return count_subarrays
    
    #  def subarraySum(self, nums: List[int], k: int) -> int:
    #     """ Neetcode: prefix_sumO(n), O(n) """
    #     res = 0
    #     curSum = 0
    #     prefixSums = {0 : 1}
    #     for num in nums:
    #         curSum += num 
    #         diff = curSum - k

    #         res += prefixSums.get(diff, 0)
    #         prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

    #     return res 

    def subarraySum(self, nums: List[int], k: int) -> int:
        """ practice: Neetcode: prefix_sum O(n), O(n) """    
        res = 0
        curSum = 0
        prefixSums = {0: 1}
        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        return res

    # # Modified Code to Find Subarrays
    # def subarraySum(nums: List[int], k: int) -> List[List[int]]:
    #     result = []  # To store the subarrays
    #     curSum = 0
    #     prefixSums = {0: [-1]}  # Initialize with 0 mapped to a list containing -1 (before the array starts)

    #     for i, num in enumerate(nums):
    #         curSum += num
    #         diff = curSum - k

    #         # If diff exists in prefixSums, it means there are subarrays ending at index `i` that sum to `k`
    #         if diff in prefixSums:
    #             for start_idx in prefixSums[diff]:
    #                 result.append(nums[start_idx + 1:i + 1])

    #         # Add the current sum to prefixSums
    #         if curSum not in prefixSums:
    #             prefixSums[curSum] = []
    #         prefixSums[curSum].append(i)

    #     return result
    
# @lc code=end

# nums = [3, 4, 7, 2, -3, , 1, 4, 2]; k = 7
# pref_sum = [3, 7, 14, 16, 13, 14, 18, 20]
# diff cumSum - k = [-4, 0, 7, 9, 6, 11, 13]

res = 0
curSum = 0
prefixSums = {0: 1}
it1: num = 3
curSum = 3
diff = curSum - k = 3 - 7 = -4
res = 0 + prefixSums.get(-4, 0) = 0
prefixSums = {0: 1, 3: 1}
it2: num = 4
curSum = 3 + 4 = 7
diff = curSum - k = 7 - 7 = 0
res = 0 + prefixSums.get(0, 0) = 0 + 1 = 1
prefixSums = {0: 1, 3: 1, 7: 1}
it3: num = 7
curSum = 7 + 7 = 14
diff = curSum - k = 14 - 7 = 7
res = 1 + prefixSums.get(7, 0) = 1 + 1 = 2
prefixSums = {0: 1, 3: 1, 7: 1, 14: 1}
it4: num = 2
curSum = 14 + 2 = 16
diff = curSum - k = 16 - 7 = 9
res = 2 + prefixSums.get(9, 0) = 2 + 0 = 2
prefixSums = {0: 1, 3: 1, 7: 1, 14: 1, 16: 1}
it5: num = -3
curSum = 16 - 3 = 13
diff = curSum - k = 13 - 7 = 6
res = 2 + prefixSums.get(6, 0) = 2 + 0 = 2
prefixSums = {0: 1, 3: 1, 7: 1, 14: 1, 16: 1, 13: 1}
it6: num = 1
curSum = 13 + 1 = 14
diff = curSum - k = 14 - 7 = 7
res = 2 + prefixSums.get(7, 0) = 2 + 1 = 3
prefixSums = {0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1}
it7: num = 4
curSum = 14 + 4 = 18
diff = curSum - k = 18 - 7 = 11
res = 3 + prefixSums.get(9, 0) = 3 + 0 = 3
prefixSums = {0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1, 18: 1}
it8: num = 2
curSum = 18 + 2 = 20
diff = curSum - k = 20 - 7 = 13
res = 3 + prefixSums.get(11, 0) = 3 + 1 = 4
prefixSums = {0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1, 18: 1, 20: 1}


# Modified Code to Find Subarrays
from typing import List

def subarraySum(nums: List[int], k: int) -> List[List[int]]:
    result = []  # To store the subarrays
    curSum = 0
    prefixSums = {0: [-1]}  # Initialize with 0 mapped to a list containing -1 (before the array starts)

    for i, num in enumerate(nums):
        curSum += num
        diff = curSum - k

        # If diff exists in prefixSums, it means there are subarrays ending at index `i` that sum to `k`
        if diff in prefixSums:
            for start_idx in prefixSums[diff]:
                result.append(nums[start_idx + 1:i + 1])

        # Add the current sum to prefixSums
        if curSum not in prefixSums:
            prefixSums[curSum] = []
        prefixSums[curSum].append(i)

    return result

# Example Usage
nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # Output: [[1, 1], [1, 1]]

# Explanation
# prefixSums Dictionary:

# Keeps track of all indices where a particular prefix sum occurs.
# This helps find all possible starting indices for subarrays that sum to k.
# Key Modifications:

# Instead of just counting the number of subarrays (res += prefixSums.get(diff, 0)), we iterate through the indices stored in prefixSums[diff] and extract the subarrays.
# Store the subarrays in the result list.
# Initialization:

# The prefixSums dictionary starts with 0: [-1] because a subarray starting from the beginning of the array needs to be handled.
# Construction of Subarrays:

# For each valid starting index stored in prefixSums[diff], the subarray is extracted using slicing: nums[start_idx + 1:i + 1].

# Complexity
# Time Complexity: O(n^2) in the worst case, because slicing the array for subarray construction takes 
# O(n) for all matches.
# Space Complexity: O(n) for the prefixSums dictionary.
    
Example Walkthrough
Input: nums = [1, 1, 1], k = 2

Step-by-Step Execution:
Initialization: curSum = 0, prefixSums = {0: [-1]}, result = [].
Iteration 1 (i=0, num=1):
curSum = 1.
diff = curSum - k = 1 - 2 = -1 (not in prefixSums).
Update prefixSums: {0: [-1], 1: [0]}.
Iteration 2 (i=1, num=1):
curSum = 2.
diff = curSum - k = 2 - 2 = 0 (exists in prefixSums at [-1]).
Add subarray: nums[0:2] = [1, 1] to result.
Update prefixSums: {0: [-1], 1: [0], 2: [1]}.
Iteration 3 (i=2, num=1):
curSum = 3.
diff = curSum - k = 3 - 2 = 1 (exists in prefixSums at [0]).
Add subarray: nums[1:3] = [1, 1] to result.
Update prefixSums: {0: [-1], 1: [0], 2: [1], 3: [2]}.
Final Result: [[1, 1], [1, 1]].