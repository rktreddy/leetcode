#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     """ Approach: Post Order DFS O(n), O(n) """
    #     maxPath = -float("inf")

    #     # post order traversal of subtree rooted at `node`
    #     def gainFromSubtree(node: Optional[TreeNode]) -> int:
    #         nonlocal maxPath

    #         if not node:
    #             return 0

    #         # add the gain from the left subtree. Note that if the
    #         # gain is negative, we can ignore it, or count it as 0.
    #         # This is the reason we use `max` here.
    #         gainFromLeft = max(gainFromSubtree(node.left), 0)

    #         # add the gain / path sum from right subtree. 0 if negative
    #         gainFromRight = max(gainFromSubtree(node.right), 0)

    #         # if left or right gain are negative, they are counted
    #         # as 0, so this statement takes care of all four scenarios
    #         maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)

    #         # return the max sum for a path starting at the root of subtree
    #         return max(gainFromLeft + node.val, gainFromRight + node.val)

    #     gainFromSubtree(root)
    #     return maxPath
    
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     """ practice: Approach: Post Order DFS O(n), O(n) """
    #     maxPath = float("-inf")
    #     def gainFromSubtree(node):
    #         nonlocal maxPath
    #         if not node:
    #             return 0
    #         leftGain = max(gainFromSubtree(node.left), 0)
    #         rightGain = max(gainFromSubtree(node.right), 0)

    #         maxPath = max(maxPath, leftGain + rightGain + node.val)

    #         return max(leftGain + node.val, rightGain + node.val)
        
    #     gainFromSubtree(root)
    #     return maxPath
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """ practice: Approach: Post Order DFS O(n), O(n) """
        maxPath = float("-inf")
        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0
            
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            maxPath = max(maxPath, left_sum + right_sum + node.val)

            return max(left_sum + node.val, right_sum + node.val)
        
        dfs(root)
        return maxPath

    # def __init__(self) -> None:
    #     self.maxPath = float("-inf")

    # def gainFromSubtree(self, node):
    #     if not node:
    #         return 0
    #     gainFromLeft = max(self.gainFromSubtree(node.left), 0)
    #     gainFromRight = max(self.gainFromSubtree(node.right), 0)
    #     self.maxPath = max(self.maxPath, gainFromLeft + gainFromRight + node.val)

    #     return max(gainFromLeft + node.val, gainFromRight + node.val)

    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     """ practice2: Approach: Post Order DFS O(n), O(n) """
    #     self.gainFromSubtree(root)
    #     return self.maxPath
    
# @lc code=end

# # practice
# def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#     diameter = 0
#     def dfs(node):
#         nonlocal diameter
#         if not node:
#             return 0

#         left_depth = dfs(node.left)
#         right_depth = dfs(node.right)

#         diameter = max(diameter, left_depth + right_depth)

#         return 1 + max(left_depth, right_depth)

#     dfs(root)
#     return diameter

