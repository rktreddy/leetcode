#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    # # Approach 1: Using a Stack and String Builder O(n), O(n)
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     indexes_to_remove = set()
    #     stack = []
    #     for i, c in enumerate(s):
    #         if c not in "()":
    #             continue
    #         if c == "(":
    #             stack.append(i)
    #         elif not stack:
    #             indexes_to_remove.add(i)
    #         else:
    #             stack.pop()
    #     indexes_to_remove = indexes_to_remove.union(set(stack))
    #     string_builder = []
    #     for i, c in enumerate(s):
    #         if i not in indexes_to_remove:
    #             string_builder.append(c)

    #     return "".join(string_builder)
        
    # #Approach 2: Two Pass String Builder O(n), O(n)
    # def minRemoveToMakeValid(self, s: str) -> str:

    #     def delete_invalid_closing(string, open_symbol, close_symbol):
    #         sb = []
    #         balance = 0
    #         for c in string:
    #             if c == open_symbol:
    #                 balance += 1
    #             if c == close_symbol:
    #                 if balance == 0:
    #                     continue
    #                 balance -= 1
    #             sb.append(c)
    #         return "".join(sb)

    #     # Note that s[::-1] gets the reverse of s.
    #     s = delete_invalid_closing(s, "(", ")")
    #     s = delete_invalid_closing(s[::-1], ")", "(")
    #     return s[::-1]

    # # Approach 3: Shortened Two Pass String Builder O(n), O(n)
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     # Pass 1: Remove all invalid ")"
    #     first_pass_chars = []
    #     balance = 0
    #     open_seen = 0
    #     for c in s:
    #         if c == "(":
    #             balance += 1
    #             open_seen += 1
    #         if c == ")":
    #             if balance == 0:
    #                 continue
    #             balance -= 1
    #         first_pass_chars.append(c)

    #     # Pass 2: Remove the rightmost "("
    #     result = []
    #     open_to_keep = open_seen - balance
    #     for c in first_pass_chars:
    #         if c == "(":
    #             open_to_keep -= 1
    #             if open_to_keep < 0:
    #                 continue
    #         result.append(c)

    #     return "".join(result)

    # # best voted leetcode O(n), O(n)
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     s = list(s)
    #     stack = []
    #     for i, char in enumerate(s):
    #         if char == "(":
    #             stack.append(i)
    #         elif char == ")":
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 s[i] = ""
    #     while stack:
    #         s[stack.pop()] = ""
    #     return ''.join(s)
    
    # # Neetcode solution 
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     res = []
    #     cnt = 0 # extra ( parantheses
    #     for c in s:
    #         if c == "(":
    #             res.append(c)
    #             cnt += 1
    #         elif c == ")" and cnt > 0:
    #             res.append(c)
    #             cnt -= 1
    #         elif c != ")":
    #             res.append(c)

    #     filtered = []
    #     for c in res[::-1]:
    #         if c == "(" and cnt > 0:
    #             cnt -= 1
    #         else:
    #             filtered.append(c)
    #     return "".join(filtered[::-1])

    # def minRemoveToMakeValid(self, s: str) -> str:
    #     """  ChatGPT solution O(n), O(n) """
    #     # First pass: Remove invalid closing parentheses
    #     stack = []
    #     to_remove = set()

    #     for i, char in enumerate(s):
    #         if char == '(':
    #             stack.append(i)  # Record the index of the opening parenthesis
    #         elif char == ')':
    #             if stack:
    #                 stack.pop()  # Valid pair found
    #             else:
    #                 to_remove.add(i)  # Unmatched closing parenthesis

    #     # Add unmatched opening parentheses to the removal set
    #     to_remove.update(stack)

    #     # Second pass: Build the result string
    #     result = []
    #     for i, char in enumerate(s):
    #         if i not in to_remove:
    #             result.append(char)

    #     return ''.join(result)

    # def minRemoveToMakeValid(self, s: str) -> str:
    #     """  practice: ChatGPT solution O(n), O(n) """
    #     stack = []
    #     to_remove = set()

    #     for i, c in enumerate(s):
    #         if c == '(':
    #             stack.append(i)
    #         elif c == ')':
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 to_remove.add(i)

    #     to_remove.update(stack)

    #     res = []
    #     for i, c in enumerate(s):
    #         if i not in to_remove:
    #             res.append(c)
    #     return ''.join(res)
    
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     """  practice: ChatGPT solution O(n), O(n) """
    #     stack = []
    #     to_remove = set()

    #     for i, c in enumerate(s):
    #         if c == '(':
    #             stack.append(i)
    #         elif c == ')':
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 to_remove.add(i)

    #     to_remove.update(stack)

    #     res = []
    #     for i, c in enumerate(s):
    #         if i not in to_remove:
    #             res.append(c)
    #     return ''.join(res)
    
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     """  
    #     ChatGPT hybrid solution O(n), O(n) 
    #     better performance and clarity
    #     Two-pass approach with stack to track unmatched '('
    #     and direct marking of invalid ')' during the first pass.
    #     """

    #     s = list(s)
    #     stack = []

    #     # Identify unmatched parentheses
    #     for i, c in enumerate(s):
    #         if c == '(':
    #             stack.append(i)
    #         elif c == ')':
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 s[i] = ''  # mark invalid ')'

    #     # Mark any unmatched '('
    #     for i in stack:
    #         s[i] = ''

    #     return ''.join(s)
    
    def minRemoveToMakeValid(self, s: str) -> str:
        """  
        practice: ChatGPT hybrid solution O(n), O(n) 
        """
        s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        for i in stack:
            s[i] = ''
        return ''.join(s)

 
# @lc code=end

# # Example Usage
# s = "a)b(c)d"
# print(minRemoveToMakeValid(s))  # Output: "ab(c)d"

