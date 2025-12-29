#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    # def isValid(self, s: str) -> bool:
    #     """ Approach 1: Stacks O(n), O(n) """
    #     stack = []
    #     mapping = {")" : "(", "}" : "{", "]" : "["}

    #     for c in s:
    #         if c in mapping:
    #             top_el = stack.pop() if stack else "#"
    #             if mapping[c] != top_el:
    #                 return False
    #         else:
    #             stack.append(c)
    #     return stack == []
    
    def isValid(self, s: str) -> bool:
        """ practice: Approach 1: Stacks O(n), O(n) """
        stack = []
        mapping = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if c in mapping:
                top_element = stack.pop() if stack else '#'
                if top_element != mapping[c]:
                    return False
            else:
                stack.append(c)
        return not stack

# @lc code=end

