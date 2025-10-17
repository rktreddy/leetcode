#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sort the array first to apply the two-pointer technique
        nums.sort()
      
        # Initialize two pointers, one at the start and one at the end
        left, right = 0, len(nums) - 1
      
        # Initialize a counter to keep track of valid operations
        operations_count = 0
      
        # Iterate through the list with two pointers
        while left < right:
            # Calculate the sum of elements pointed by left and right
            sum_of_pair = nums[left] + nums[right]
          
            # If the sum equals k, we found a valid pair
            if sum_of_pair == k:
                # Increment the count of valid operations
                operations_count += 1
                # Move both pointers towards the center
                left += 1
                right -= 1
            # If the sum is too large, move the right pointer to the left
            elif sum_of_pair > k:
                right -= 1
            # If the sum is too small, move the left pointer to the right
            else:
                left += 1
      
        # Return the total count of valid operations
        return operations_count
        
# @lc code=end

