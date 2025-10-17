#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    # def isHappy(self, n: int) -> bool:
    #     """ Approach 1: Detect Cycles with a HashSet O(log n), O(logn)"""
    #     def get_next(n):
    #         total_sum = 0
    #         while n > 0:
    #             n, digit = divmod(n, 10)
    #             total_sum += digit ** 2
    #         return total_sum
    #     seen = set()
    #     while n != 1 and n not in seen:
    #         seen.add(n)
    #         n = get_next(n)
    #     return n == 1

    def isHappy(self, n: int) -> bool:
        """ Approach 2: Floyd's Cycle-Finding Algorithm O(log n), O(1)"""
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1


# @lc code=end

