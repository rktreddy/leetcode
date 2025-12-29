#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    # def removeDuplicates(self, s: str) -> str:
    #     """ Approach 1: Replace O(n^2), O(n^2) """
    #     # generate 26 possible duplicates
    #     duplicates = {2 * ch for ch in ascii_lowercase}
        
    #     prev_length = -1
    #     while prev_length != len(S):
    #         prev_length = len(S)
    #         for d in duplicates:
    #             S = S.replace(d, '')
                
    #     return S
    
    # def removeDuplicates(self, s: str) -> str:
    #     """ Approach 2: Stack O(n), O(n - d) """
        
    #     output = []
    #     for ch in s:
    #         if output and ch == output[-1]: 
    #             output.pop()
    #         else: 
    #             output.append(ch)
    #     return ''.join(output)
    

    # def removeDuplicates(self, s: str) -> str:
    #     """ practice: Approach 2: Stack O(n), O(n - d) """
    #     stack = []
    #     for c in s:
    #         if stack and c == stack[-1]:
    #             stack.pop()
    #         else:
    #             stack.append(c)
    #     return ''.join(stack)
    
    def removeDuplicates(self, s: str) -> str:
        """ practice: Approach 2: Stack O(n), O(n - d) """
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

        
# @lc code=end

