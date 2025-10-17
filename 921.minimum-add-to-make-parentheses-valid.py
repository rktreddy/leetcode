#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    # def minAddToMakeValid(self, s: str) -> int:
    #     """ Approach 1: Balance O(N), O(1) """
    #     ans = bal = 0 
    #     for symbol in s:
    #         bal += 1 if symbol == '(' else -1
    #         if bal == -1:
    #             bal += 1
    #             ans += 1
    #     return ans + bal 
    
    # def minAddToMakeValid(self, s: str) -> int:
    #     """ Approach 2: Top voted on LC """
    #     stack = []
    #     for ch in s:
    #         if ch == '(': stack.append(ch)
    #         else:
    #             if len(stack) and stack[-1] == '(': stack.pop()
    #             else: stack.append(ch)
    #     return len(stack)

    # def minAddToMakeValid(self, s: str) -> int:
    #     """ Approach: Open Bracket Counter O(n), O(1) """
    #     open_brackets = 0
    #     min_adds_required = 0

    #     for c in s:
    #         if c == "(":
    #             open_brackets += 1
    #         else:
    #             if open_brackets > 0:
    #                 open_brackets -= 1
    #             else:
    #                 min_adds_required += 1

    #     # Add the remaining open brackets as closing brackets would be required.
    #     return min_adds_required + open_brackets

    def minAddToMakeValid(self, s: str) -> int:
        """ practice: Approach: Open Bracket Counter O(n), O(1) """
        open_pare = 0
        min_adds = 0
        for c in s:
            if c == '(':
                open_pare += 1
            else:
                if open_pare > 0:
                    open_pare -= 1
                else:
                    min_adds += 1
        return open_pare + min_adds


# @lc code=end

