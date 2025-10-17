#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
class Solution:
    # def arrayPairSum(self, nums: List[int]) -> int:
    #     """ Approach 1: Sorting O(nlogn), O(n) """
    #     # Sort the list in ascending order
    #     nums.sort()
    #     # Initialize sum to zero
    #     max_sum = 0
    #     for i in range(0, len(nums), 2):
    #         # Add every element at even positions (0-indexed)
    #         max_sum += nums[i]
            
    #     return max_sum

    def arrayPairSum(self, nums: List[int]) -> int:
        """ Approach 2: Counting Sort O(n+k), O(k): n #pairs, k #range """
        K = 10000
        # Store the frequency of each element
        element_to_count = [0] * (2 * K + 1)
        for element in nums:
            # Add K to element to offset negative values
            element_to_count[element + K] += 1
            
        # Initialize sum to zero
        max_sum = 0
        is_even_index = True
        for element in range(2 * K + 1):
            while element_to_count[element] > 0 :
                # Add element if it is at even index
                if is_even_index:
                    max_sum += element - K
                # Flip the value (one to zero or zero to one)
                is_even_index = not is_even_index;
                # Decrement the frequency count
                element_to_count[element] -= 1
        return max_sum
        
# @lc code=end

