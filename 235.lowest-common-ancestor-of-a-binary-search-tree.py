#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # Recursive approach O(N), O(N)
    #     parent_val = root.val
    #     p_val = p.val
    #     q_val = q.val

    #     if p_val > parent_val and q_val > parent_val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     elif p_val < parent_val and q_val < parent_val:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     else:
    #         return root

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     """ Iterative approach O(N), O(1) """
        
    #     p_val = p.val
    #     q_val = q.val

    #     node = root
    #     while node:
    #         parent_val = node.val
    #         if p_val > parent_val and q_val > parent_val:
    #             node = node.right
    #         elif p_val < parent_val and q_val < parent_val:
    #             node = node.left
    #         else:
    #             return node
            
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     """ practice: Iterative approach """
    #     while root:
    #         if p.val < root.val and q.val < root.val:
    #             root = root.left
    #         elif p.val > root.val and q.val > root.val:
    #             root = root.right
    #         else:
    #             return root
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ practice: Iterative approach """
        while root:
            if p.val < root.val and q.val < root. val:
                root = root.left
            elif p.val > root.val and q.val > root. val:
                root = root.right
            else:
                return root

# @lc code=end

