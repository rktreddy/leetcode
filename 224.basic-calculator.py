#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    # def evaluate_expr(self, stack):

    #     if not stack or type(stack[-1]) == str:
    #         stack.append(0)

    #     res = stack.pop()

    #     while stack and stack[-1] != ')':
    #         sign = stack.pop()
    #         if sign == '+':
    #             res += stack.pop()
    #         else:
    #             res -= stack.pop()

    #     return res
    # def calculate(self, s: str) -> int:
    #     """ Approach 1: Stack and String Reversal O(N), O(N) """

    #     stack = []
    #     n, operand = 0, 0

    #     for i in range(len(s) - 1, -1, -1):
    #         ch = s[i]

    #         if ch.isdigit():
    #             operand = (10 ** n * int(ch)) + operand
    #             n += 1
                
    #         elif ch != " ":
    #             if n:
    #                 stack.append(operand)
    #                 n, operand = 0, 0

    #             if ch == '(':
    #                 res = self.evaluate_expr(stack)
    #                 stack.pop()

    #                 stack.append(res)

    #             else:
    #                 stack.append(ch)

    #     if n:
    #         stack.append(operand)
        
    #     return self.evaluate_expr(stack)
                    
    # def calculate(self, s: str) -> int:
    #     """ Approach 2: Stack and No String Reversal """

    #     stack = []
    #     operand = 0
    #     res = 0 # For the on-going result
    #     sign = 1 # 1 means positive, -1 means negative  

    #     for ch in s:
    #         if ch.isdigit():

    #             # Forming operand, since it could be more than one digit
    #             operand = (operand * 10) + int(ch)

    #         elif ch == '+':

    #             # Evaluate the expression to the left,
    #             # with result, sign, operand
    #             res += sign * operand

    #             # Save the recently encountered '+' sign
    #             sign = 1

    #             # Reset operand
    #             operand = 0

    #         elif ch == '-':

    #             res += sign * operand
    #             sign = -1
    #             operand = 0

    #         elif ch == '(':

    #             # Push the result and sign on to the stack, for later
    #             # We push the result first, then sign
    #             stack.append(res)
    #             stack.append(sign)

    #             # Reset operand and result, as if new evaluation begins for the new sub-expression
    #             sign = 1
    #             res = 0

    #         elif ch == ')':

    #             # Evaluate the expression to the left
    #             # with result, sign and operand
    #             res += sign * operand

    #             # ')' marks end of expression within a set of parenthesis
    #             # Its result is multiplied with sign on top of stack
    #             # as stack.pop() is the sign before the parenthesis
    #             res *= stack.pop() # stack pop 1, sign

    #             # Then add to the next operand on the top.
    #             # as stack.pop() is the result calculated before this parenthesis
    #             # (operand on stack) + (sign on stack * (result from parenthesis))
    #             res += stack.pop() # stack pop 2, operand

    #             # Reset the operand
    #             operand = 0

    #     return res + sign * operand
    
    # def calculate(self, s: str) -> int:
    #     """ practice: Approach 2: Stack and No String Reversal O(n), O(n) """
    #     stack = []
    #     res = cur = 0
    #     sign = 1 # 1 if + else -1
    #     for c in s:
    #         if c.isdigit():
    #             cur = cur * 10 + int(c)
    #         elif c in '+-':
    #             res += sign * cur
    #             sign = 1 if c == '+' else -1
    #             cur = 0
    #         elif c == '(':
    #             stack.append(res)
    #             stack.append(sign)
    #             sign = 1
    #             res = 0
    #         elif c == ')':
    #             res += sign * cur
    #             res *= stack.pop()
    #             res += stack.pop()
    #             cur = 0
    #     return res + sign * cur
    
    def calculate(self, s: str) -> int:
        """ practice: Approach 2: Stack and No String Reversal O(n), O(n) """
        res = cur = 0
        sign = 1 # 1 if '+' else -1
        stack = []
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in '+-':
                res += sign * cur
                sign = 1 if c == '+' else -1
                cur = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + sign * cur
    


# @lc code=end

