#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    # def simplifyPath(self, path: str) -> str:
    #     """ Approach: Using Stacks O(N), O(N) """

    #     # Initialize a stack
    #     stack = []

    #     # Split the input string on "/" as the delimiter
    #     # and process each portion one by one
    #     for portion in path.split("/"):

    #         # If the current component is a "..", then
    #         # we pop an entry from the stack if it's non-empty
    #         if portion == "..":
    #             if stack:
    #                 stack.pop()
    #         elif portion == "." or not portion:
    #             # A no-op for a "." or an empty string
    #             continue
    #         else:
    #             # Finally, a legitimate directory name, so we add it
    #             # to our stack
    #             stack.append(portion)

    #     # Stich together all the directory names together
    #     final_str = "/" + "/".join(stack)
    #     return final_str
    
    # def simplifyPath(self, path: str) -> str:
    #     """ practice: Approach: Using Stacks O(N), O(N) """
    #     stack = []
    #     for part in path.split("/"):
    #         if part == '..':
    #             if stack:
    #                 stack.pop()
    #         elif part == '.' or part == '':
    #             continue
    #         else:
    #             stack.append(part)

    #     return '/' + '/'.join(stack)
    
    def simplifyPath(self, path: str) -> str:
        """ practice: Approach: Using Stacks O(N), O(N) """
        stack = []
        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or part == "":
                continue
            else:
                stack.append(part)
        return "/" + "/".join(stack)

# @lc code=end

