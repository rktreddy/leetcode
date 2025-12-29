#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     """ my initial trial """
    #     stack = []
    #     hashmap = {}
    #     for temp in temperatures:
    #         count = 0
    #         while stack and temp < stack[-1]:
    #             count += 1
    #         hashmap[stack.pop()] = count
    #         stack.append(temp)

    #     while stack:
    #         hashmap[stack.pop()] = 0

    #     return [hashmap.get(i, 0) for i in temperatures]
    
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     """ Bruteforce O(n^2),  """
    #     n = len(temperatures)
    #     answer = [0] * n
    #     for day in range(n):
    #         for future_day in range(day + 1, n):
    #             if temperatures[future_day] > temperatures[day]:
    #                 answer[day] = future_day - day
    #                 break      
                
    #     return answer
    
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     """ Approach 1: Monotonic Stack O(n), O(n) """
    #     n = len(temperatures)
    #     answer = [0] * n 
    #     stack = []

    #     for curr_day, curr_temp in enumerate(temperatures):
    #         # Pop until the current day's temperature is not
    #         # warmer than the temperature at the top of the stack
    #         while stack and temperatures[stack[-1]] < curr_temp:
    #             prev_day = stack.pop()
    #             answer[prev_day] = curr_day - prev_day
    #         stack.append(curr_day)

    #     return answer
    
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     """ practice: Approach 1: Monotonic Stack O(n), O(n) """
    #     n = len(temperatures)
    #     answer = [0] * n
    #     stack = []
    #     for curr_day, curr_temp in enumerate(temperatures):
    #         while stack and temperatures[stack[-1]] < curr_temp:
    #             prev_day = stack.pop()
    #             answer[prev_day] = curr_day - prev_day
    #         stack.append(curr_day)
    #     return answer
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ cracking fancg Approach 1: Monotonic Stack O(n), O(n) """
        stack = []
        res = [0] * len(temperatures)
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur_temp:
                prev_day = stack.pop()
                res[prev_day] = cur_day - prev_day
            stack.append(cur_day)
        return res
    
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     """ Approach 2: Array, Optimized Space O(n), O(1) """
    #     n = len(temperatures)
    #     hottest = 0
    #     answer = [0] * n 

    #     for curr_day in range(n - 1, -1, -1):
    #         curr_temp = temperatures[curr_day]
    #         if curr_temp >= hottest:
    #             hottest = curr_temp
    #             continue    

    #         days = 1
    #         while temperatures[curr_day + days] <= curr_temp:
    #             days += answer[curr_day + days]
    #         answer[curr_day] = days

    #     return answer
            

        
# @lc code=end

