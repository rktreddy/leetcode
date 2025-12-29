#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def height(self, root):
    #     # An empty tree has height -1
    #     if not root:
    #         return -1
    #     return 1 + max(self.height(root.left), self.height(root.right))
    
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     # An empty tree satisfies the definition of a balanced tree
    #     if not root:
    #         return True
        
    #     return (
    #         abs(self.height(root.left) - self.height(root.right)) < 2
    #         and self.isBalanced(root.left)
    #         and self.isBalanced(root.right)
    #     )
        
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     """ Neetcode Recursive DFS O(n), O(h) """
    #     def dfs(root):
    #         if not root:
    #             return [True, 0]

    #         left, right = dfs(root.left), dfs(root.right)
    #         balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
    #         return [balanced, 1 + max(left[1], right[1])]

    #     return dfs(root)[0]
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """ practice: Neetcode Recursive DFS O(n), O(h) """
        def dfs(node):
            if not node:
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
    

# @lc code=end

