#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    # def calculate(self, s: str) -> int:
    #     """ https://walkccc.me/LeetCode/problems/227/#__tabbed_2_3 """
    #     """ Approach 1: Similar to 772. Basic Calculator III O(n), O(n) """
    #     ans = 0
    #     prevNum = 0
    #     currNum = 0
    #     op = '+'

    #     for i, c in enumerate(s):
    #         if c.isdigit():
    #                currNum = currNum * 10 + int(c)
    #         if not c.isdigit() and c != ' ' or i == len(s) - 1:
    #             if op == '+' or op == '-':
    #                 ans += prevNum
    #                 prevNum = currNum if op == '+' else -currNum
    #             elif op == '*':
    #                 prevNum = prevNum * currNum
    #             elif op == '/':
    #                 if prevNum < 0:
    #                     prevNum = math.ceil(prevNum / currNum)
    #                 else:
    #                     prevNum = prevNum // currNum
    #             op = c
    #             currNum = 0

    #     return ans + prevNum
    
    # def calculate(self, s: str) -> int:
    #     """ Approach 2: O(n), O(1)"""
    #     ans = 0
    #     prevNum = 0
    #     currNum = 0
    #     op = '+'

    #     for i, c in enumerate(s):
    #         if c.isdigit():
    #             currNum = currNum * 10 + int(c)
    #         if not c.isdigit() and c != ' ' or i == len(s) - 1:
    #             if op == '+' or op == '-':
    #                 ans += prevNum
    #                 prevNum = (currNum if op == '+' else -currNum)
    #             elif op == '*':
    #                 prevNum *= currNum
    #             elif op == '/':
    #                 prevNum = int(prevNum / currNum)
    #             op = c
    #             currNum = 0

    #     return ans + prevNum
        
    # def calculate(self, s: str) -> int:
    #     """ Using stack: O(n), O(n) """
    #     # Initialize the value to hold current number and stack to store values.
    #     value, n = 0, len(s)
    #     # Set the initial sign to '+' (plus).
    #     sign = '+'
    #     # Initialize an empty stack to keep numbers and intermediate results.
    #     stack = []

    #     # Iterate over each character in the input string.
    #     for i, char in enumerate(s):
    #         # If the character is a digit, update 'value' to be the current multi-digit number.
    #         if char.isdigit():
    #             value = value * 10 + int(char)
          
    #         # If we reach the end of the string or encounter an operator.
    #         if i == n - 1 or char in '+-*/':
    #             # Perform an action depending on the last sign observed.
    #             if sign == '+':
    #                 # If the sign is plus, push the current value onto the stack.
    #                 stack.append(value)
    #             elif sign == '-':
    #                 # If the sign is minus, push the negative of the value onto the stack.
    #                 stack.append(-value)
    #             elif sign == '*':
    #                 # If the sign is times, multiply the top of the stack by the current value and push it back.
    #                 stack.append(stack.pop() * value)
    #             elif sign == '/':
    #                 # If the sign is divide, take the top of the stack, divide by current value and push the result back.
    #                 # Use integer division to round towards zero.
    #                 stack.append(int(stack.pop() / value))
              
    #             # Update the sign to the current operator.
    #             sign = char
    #             # Reset 'value' for the next number.
    #             value = 0
      
    #     # The final result is the sum of the values in the stack.
    #     return sum(stack)

    # def calculate(self, s: str) -> int:
    #     """ practice: Using stack: O(n), O(n) """
    #     value, n = 0, len(s)
    #     sign = '+'
    #     stack = []

    #     for i, char in enumerate(s):
    #         if char.isdigit():
    #             value = value * 10 + int(char)

    #         if i == n - 1 or char in '+-*/':
    #             if sign == '+':
    #                 stack.append(value)
    #             elif sign == '-':
    #                 stack.append(-value)
    #             elif sign == '*':
    #                 stack.append(stack.pop() * value)
    #             elif sign == '/':
    #                 stack.append(int(stack.pop() / value))

    #             sign = char
    #             value = 0
    #     return sum(stack)
    
    # def calculate(self, s: str) -> int:
    #     """ ChatGPT: Iterative approach: O(n) time, O(1) space"""
    #     result = 0
    #     last_value = 0
    #     value = 0
    #     sign = '+'
    #     n = len(s)

    #     for i, char in enumerate(s):
    #         if char.isdigit():
    #             value = value * 10 + int(char)  # Build the current number

    #         # Process at the end of the string or when an operator is encountered
    #         if i == n - 1 or char in '+-*/':
    #             if sign == '+':
    #                 result += last_value  # Add the previous number to the result
    #                 last_value = value  # Update the last_value to the current number
    #             elif sign == '-':
    #                 result += last_value
    #                 last_value = -value
    #             elif sign == '*':
    #                 last_value *= value  # Multiply the last_value by the current number
    #             elif sign == '/':
    #                 # Perform integer division (truncate toward zero)
    #                 last_value = int(last_value / value)

    #             sign = char  # Update the current sign
    #             value = 0  # Reset value for the next number

    #     result += last_value  # Add the last processed number to the result
    #     return result


    # def calculate(self, s: str) -> int:
    #     """ practice: Without Using stack: O(n), O(1) """
    #     last_val, val = 0, 0
    #     n = len(s)
    #     sign = '+'
    #     ans = 0

    #     for i, c in enumerate(s):
    #         if c.isdigit():
    #             val = val * 10 + int(c)

    #         if i == n - 1 or c in '+-*/':
    #             if sign == '+' or sign == '-':
    #                 ans += last_val
    #                 last_val = val if sign == '+' else -val
    #             elif sign == '*':
    #                 last_val *= val
    #             elif sign == '/':
    #                 last_val = int(last_val / val)

    #             sign = c
    #             val = 0

    #     ans += last_val
    #     return ans
    
    def calculate(self, s: str) -> int:
        """ practice: Without Using stack: O(n), O(1) """
        last_val, val, ans = 0, 0, 0
        sign = '+'
        n = len(s)

        for i, c in enumerate(s):
            if c.isdigit():
                val = val * 10 + int(c)

            if i == n - 1 or c in '+-*/':
                if sign == '+' or sign == '-':
                    ans += last_val
                    last_val = val if sign == '+' else -val
                elif sign == '*':
                    last_val *= val
                elif sign == '/':
                    last_val = int(last_val / val)

                sign = c
                val = 0

        ans += last_val
        return ans

    
# @lc code=end

s = "3+2*2"
last_value = 9, value=0, n = 5
sign = '+', answer = 0
i = 0, char = 3
value = 0 * 10 + 3 = 3
last_value = 0; answer = 0
i = 1, char = '+'
value = 3
sign = '+'
answer = 0 + 0 = 0
last_value = value = 3
value = 0, sign = '+'
i = 2, char = 2
value = 0 * 10 + 2 = 2
answer = 0; last_value = 3
i = 3, char = '*'
value = 2
answer = 0 + 3 = 3
last_value = value = 2
sign = '*', value = 0

i = 4 (i == n - 1), char = 2
value = 0 * 10 + 2 = 2
last_value = 2 * 2 = 4

answer = 3 + 4 = 7

