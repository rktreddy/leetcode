#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    # def numSquares(self, n: int) -> int:
    #     """ Approach 1: Brute-force Enumeration [Time Limit Exceeded] """
    #     square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

    #     def minNumSquares(k):
    #         """ recursive solution """
    #         # bottom cases: find a square number
    #         if k in square_nums:
    #             return 1
    #         min_num = float('inf')

    #         # Find the minimal value among all possible solutions
    #         for square in square_nums:
    #             if k < square:
    #                 break
    #             new_num = minNumSquares(k-square) + 1
    #             min_num = min(min_num, new_num)
    #         return min_num

    #     return minNumSquares(n)
    
    # def numSquares(self, n: int) -> int:
    #     """ Approach 2: Dynamic Programming O(n sqrt(N)), O(n) """
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    #     dp = [float("inf")] * (n + 1)
    #     # bottom case
    #     dp[0] = 0

    #     for i in range(1, n + 1):
    #         for square in square_nums:
    #             if i < square:
    #                 break
    #             dp[i] = min(dp[i], dp[i - square] + 1)
    #     return dp[-1]
    
    # def numSquares(self, n: int) -> int:
    #     """ Approach 3: Greedy Enumeration O(n^(h/2)), O(sqrt(n)) """
    #     def is_divided_by(n, count):
    #         """
    #             return: true if "n" can be decomposed into "count" number of perfect square numbers.
    #             e.g. n=12, count=3:  true.
    #                  n=12, count=2:  false
    #         """
    #         if count == 1:
    #             return n in square_nums
            
    #         for k in square_nums:
    #             if is_divided_by(n - k, count - 1):
    #                 return True
    #         return False

    #     square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
    
    #     for count in range(1, n+1):
    #         if is_divided_by(n, count):
    #             return count

    # def numSquares(self, n: int) -> int:
    #     """ Approach 4: Greedy + BFS (Breadth-First Search) """
    #     # list of square numbers that are less than `n`
    #     square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
    #     level = 0
    #     queue = {n}
    #     while queue:
    #         level += 1
    #         #! Important: use set() instead of list() to eliminate the redundancy,
    #         # which would even provide a 5-times speedup, 200ms vs. 1000ms.
    #         next_queue = set()
    #         # construct the queue for the next level
    #         for remainder in queue:
    #             for square_num in square_nums:    
    #                 if remainder == square_num:
    #                     return level  # find the node!
    #                 elif remainder < square_num:
    #                     break
    #                 else:
    #                     next_queue.add(remainder - square_num)
    #         queue = next_queue
    #     return level
        
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq * sq == n 
    def numSquares(self, n: int) -> int:
        """ Approach 5: Mathematics O(sqrt(N)), O(1)"""
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3
    

# @lc code=end

