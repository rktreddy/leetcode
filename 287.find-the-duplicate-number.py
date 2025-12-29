#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     """ Approach 1: Sort O(nlogn) o(logn) to o(n) """
    #     nums.sort()
    #     for i in range(1, len(nums)):
    #         if nums[i] == nums[i-1]:
    #             return nums[i]
            
    # def findDuplicate(self, nums: List[int]) -> int:
    #     """ Approach 1: Set O(n), o(n) """
    #     seen = set()
    #     for num in nums:
    #         if num in seen:
    #             return num
    #         seen.add(num)

    # def findDuplicate(self, nums: List[int]) -> int:
    #     """ Approach 3: Negative Marking O(n), O(1) """
    #     for num in nums:
    #         cur = abs(num)
    #         if nums[cur] < 0:
    #             duplicate = cur
    #             break
    #         nums[cur] = -nums[cur]

    #     # Restore numbers
    #     for i in range(len(nums)):
    #         nums[i] = abs(nums[i])

        # return duplicate
    
    # def findDuplicate(self, nums: List[int]) -> int:
    #     """ Approach 4.1: Array as HashMap (Recursion) O(n), O(n) """
    #     def store(nums: List[int], cur: int) -> int:
    #         if cur == nums[cur]:
    #             return cur
    #         nxt = nums[cur]
    #         nums[cur] = cur
    #         return store(nums, nxt)
        
    #     return store(nums, 0)
    
    # def findDuplicate(self, nums: List[int]) -> int:
    #     """ Approach 4.2: Array as HashMap (Iterative) O(n), O(1) """
    #     while nums[0] != nums[nums[0]]:
    #         nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    #     return nums[0]
    

    # def findDuplicate(self, nums: List[int]) -> int:
    #     """ Approach 5: Binary Search O(nlogn), O(1) """
    #     low = 1
    #     high = len(nums) - 1
    #     while low <= high:
    #         mid = (low + high) // 2
    #         # count = 0   
    #         count = sum(num <= mid for num in nums)
    #         if count > mid:
    #             duplicate = mid
    #             high = mid - 1
    #         else:
    #             low = mid + 1

    #     return duplicate

    # def findDuplicate(self, nums: List[int]) -> int:
    #     """ Approach 6: Sum of Set Bits O(nlogn), O(1) """
    #     duplicate = 0
    #     n = len(nums) - 1
    #     bits = n.bit_length()
    #     for bit in range(bits):
    #         mask = 1 << bit
    #         base_count = 0
    #         nums_count = 0
    #         for i in range(n + 1):
    #             # If bit is set in number (i) then add 1 to base_count
    #             if i & mask:
    #                 base_count += 1
                    
    #             # If bit is set in nums[i] then add 1 to nums_count
    #             if nums[i] & mask:
    #                 nums_count += 1
                    
    #         # If the current bit is more frequently set in nums than it is in 
    #         # the range [1, 2, ..., n] then it must also be set in the duplicate number.
    #         if nums_count - base_count > 0:
    #             duplicate |= mask
                
    #     return duplicate
    
    # def findDuplicate(self, nums: List[int]) -> int:
    #     """ Approach 7: Floyd's Tortoise and Hare (Cycle Detection) O(n), O(1) """
    #     # Find the intersection point of the two runners.
    #     tortoise = hare = nums[0]
    #     while True:
    #         tortoise = nums[tortoise]
    #         hare = nums[nums[hare]]
    #         if tortoise == hare:
    #             break

    #     # Find the "entrance" to the cycle.
    #     tortoise = nums[0]
    #     while tortoise != hare:
    #         tortoise = nums[tortoise]
    #         hare = nums[hare]
        
    #     return hare

    def findDuplicate(self, nums: List[int]) -> int:
        """ Approach 7: practice: Floyd's Tortoise and Hare (Cycle Detection) O(n), O(1) """
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
            
# @lc code=end

