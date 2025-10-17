#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach 1: Bitmasking O(n 2^n), O(n 2^n) """

    #     n = len(nums)
    #     # Sort the generated subset. This will help to identify duplicates.
    #     nums.sort()
    #     maxNumberOfSubsets = 2**n
    #     # To store the previously seen sets.
    #     seen = set()
    #     subsets = []
    #     for subsetIndex in range(maxNumberOfSubsets):
    #         # Append subset corresponding to that bitmask.
    #         currentSubset = []
    #         hashcode = ""
    #         for j in range(n):
    #             # Generate the bitmask
    #             mask = 2**j
    #             isSet = mask & subsetIndex
    #             if isSet != 0:
    #                 currentSubset.append(nums[j])
    #                 # Generate the hashcode by creating a comma separated string of numbers in the currentSubset.
    #                 hashcode += str(nums[j]) + ","
    #         if hashcode not in seen:
    #             subsets.append(currentSubset)
    #             seen.add(hashcode)
    #     return subsets
    

    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     """ Approach 2: Cascading (Iterative) O(n 2^n), O(log n) """
    #     nums.sort()
    #     subsets = [[]]
    #     subsetSize = 0
    #     for i in range(len(nums)):
    #         # subsetSize refers to the size of the subset in the previous step.
    #         # This value also indicates the starting index of the subsets generated in this step.
    #         startingIndex = (
    #             subsetSize if i >= 1 and nums[i] == nums[i - 1] else 0
    #         )
    #         subsetSize = len(subsets)
    #         for j in range(startingIndex, subsetSize):
    #             currentSubset = list(subsets[j])
    #             currentSubset.append(nums[i])
    #             subsets.append(currentSubset)
    #     return subsets
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """ Approach 3: Backtracking O(n 2^n), O(n) """
        nums.sort()
        subsets = []
        currentSubset = []
        self.subsetsWithDupHelper(subsets, currentSubset, nums, 0)
        return subsets

    def subsetsWithDupHelper(self, subsets, currentSubset, nums, index):
        # Add the subset formed so far to the subsets list.
        subsets.append(list(currentSubset))
        for i in range(index, len(nums)):
            # If the current element is a duplicate, ignore.
            if i != index and nums[i] == nums[i - 1]:
                continue
            currentSubset.append(nums[i])
            self.subsetsWithDupHelper(subsets, currentSubset, nums, i + 1)
            currentSubset.pop()
        
        
# @lc code=end

