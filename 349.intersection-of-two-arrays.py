#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """ Approach 1: Sorting and Two Pointers O(nlogn + mlogn), O(m + n) """
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """
    #     # Sort both arrays
    #     nums1.sort()
    #     nums2.sort()

    #     # Initialize two pointers
    #     N = len(nums1)
    #     M = len(nums2)
    #     p1 = 0
    #     p2 = 0

    #     # Create set that stores integers appearing in both arrays
    #     intersection = set()

    #     while p1 < N and p2 < M:
    #         # Add a value to the set if values at both pointers equal
    #         if nums1[p1] == nums2[p2]:
    #             intersection.add(nums1[p1])
    #             p1 += 1
    #             p2 += 1
    #         elif nums1[p1] < nums2[p2]:
    #             p1 += 1
    #         else:
    #             p2 += 1

    #     # Convert intersection to an array
    #     result = []
    #     for x in intersection:
    #         result.append(x)

    #     # Return the result
    #     return result
    
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """ Approach 2: Built-in Set Intersection O(m + n), O(m + n) """
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """  
    #     set1 = set(nums1)
    #     set2 = set(nums2)
    #     return list(set2 & set1)
    
    
    # def set_intersection(self, set1, set2):
    #     return [x for x in set1 if x in set2]
        
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """ Approach 3: Two Sets O(m + n), O(m + n) """
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """  
    #     set1 = set(nums1)
    #     set2 = set(nums2)
        
    #     if len(set1) < len(set2):
    #         return self.set_intersection(set1, set2)
    #     else:
    #         return self.set_intersection(set2, set1)
        
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ practice: Approach 3: Two Sets O(m + n), O(m + n) """
        set1 = set(nums1)
        set2 = set(nums2)

        if len(nums1) < len(nums2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]


    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """ Approach 4: One Dictionary O(m + n) to O(m * n), O(n) """

    #     # Initialize seen dictionary and res array
    #     seen = {}
    #     result = []

    #     # mark values occurring in nums1
    #     for x in nums1:
    #       seen[x] = 1
          
    #     for x in nums2:
    #       # Check if x is in the dictionary and not in the result
    #       if x in seen and seen[x] == 1:
    #         result.append(x)
    #         seen[x] = 0

    #     # Return the result
    #     return result
    



        
# @lc code=end

