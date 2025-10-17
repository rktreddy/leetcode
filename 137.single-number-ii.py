#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     """ Approach 1: Sorting O(NlogN) , O(N) """

    #     nums.sort()

    #     for i in range(0, len(nums) - 1, 3):
    #         if nums[i] == nums[i + 1]:
    #             continue
    #         else:
    #             return nums[i]

    #     return nums[len(nums) - 1]
    
    # def singleNumber(self, nums: List[int]) -> int:
    #     """ Approach 2: Hash Map O(N), O(N) """

    #     freq = {}

    #     for num in nums:
    #         if num not in freq:
    #             freq[num] = 1
    #         else:
    #             freq[num] += 1

    #     for key in freq:
    #         if freq[key] == 1:
    #             return key
            
    # def singleNumber(self, nums: List[int]) -> int:
    #     """ Approach 3: Mathematics O(N), O(N) """
    #     return (3 * sum(set(nums)) - sum(nums)) // 2
    
    def singleNumber(self, nums: List[int]) -> int:
        """ Approach 3: Mathematics O(N), O(1) """

        # Loner.
        loner = 0

        # Iterate over all bits
        for shift in range(32):
            bit_sum = 0

            # For this bit, iterate over all integers
            for num in nums:

                # Compute the bit of num, and add it to bit_sum
                bit_sum += (num >> shift) & 1

            # Compute the bit of loner and place it
            loner_bit = bit_sum % 3
            loner = loner | (loner_bit << shift)

        # Do not mistaken sign bit for MSB.
        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner
        
# @lc code=end


