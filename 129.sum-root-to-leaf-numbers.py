#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
    #     """ Approach 1: Iterative Preorder Traversal. O(N), O(H) """
    #     root_to_leaf: int = 0
    #     stack = [(root, 0)]

    #     while stack:
    #         root, curr_number = stack.pop()
    #         if root is not None:
    #             curr_number = curr_number * 10 + root.val
    #             # if it's a leaf, update root-to-leaf sum
    #             if root.left is None and root.right is None:
    #                 root_to_leaf += curr_number
    #             else:
    #                 stack.append((root.right, curr_number))
    #                 stack.append((root.left, curr_number))

    #     return root_to_leaf

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """ practice: Approach 1: Iterative Preorder Traversal. O(N), O(H) """
        root_to_leaf = 0
        stack = [(root, 0)]
        while stack:
            node, cur = stack.pop()
            if node:
                cur = cur * 10 + node.val
                if not node.left and not node.right:
                    root_to_leaf += cur
                else:
                    stack.append((node.left, cur))
                    stack.append((node.right, cur))
        return root_to_leaf
    
    # def sumNumbers(self, root: TreeNode) -> int:
    #     """ Approach 2: Recursive Preorder Traversal. O(N), O(H) """
    #     def preorder(r: TreeNode, curr_number: int) -> None:
    #         nonlocal root_to_leaf
    #         if r:
    #             curr_number = curr_number * 10 + r.val
    #             # if it's a leaf, update root-to-leaf sum
    #             if not (r.left or r.right):
    #                 root_to_leaf += curr_number

    #             preorder(r.left, curr_number)
    #             preorder(r.right, curr_number)

    #     root_to_leaf = 0
    #     preorder(root, 0)
    #     return root_to_leaf

    # def sumNumbers(self, root):
    #     """ chatgpt: recursive dfs"""
    #     def dfs(node, curr):
    #         if not node:
    #             return 0
    #         curr = curr * 10 + node.val
    #         if not node.left and not node.right:
    #             return curr
    #         return dfs(node.left, curr) + dfs(node.right, curr)

    #     return dfs(root, 0)

    
    # def sumNumbers(self, root: TreeNode) -> int:
    #     """ Approach 3: Morris Preorder Traversal. O(N), O(1) """
    #     root_to_leaf = curr_number = 0

    #     while root:
    #         # If there is a left child,
    #         # then compute the predecessor.
    #         # If there is no link predecessor.right = root --> set it.
    #         # If there is a link predecessor.right = root --> break it.
    #         if root.left:
    #             # Predecessor node is one step to the left
    #             # and then to the right till you can.
    #             predecessor = root.left
    #             steps = 1
    #             while predecessor.right and predecessor.right is not root:
    #                 predecessor = predecessor.right
    #                 steps += 1

    #             # Set link predecessor.right = root
    #             # and go to explore the left subtree
    #             if predecessor.right is None:
    #                 curr_number = curr_number * 10 + root.val
    #                 predecessor.right = root
    #                 root = root.left
    #             # Break the link predecessor.right = root
    #             # Once the link is broken,
    #             # it's time to change subtree and go to the right
    #             else:
    #                 # If you're on the leaf, update the sum
    #                 if predecessor.left is None:
    #                     root_to_leaf += curr_number
    #                 # This part of tree is explored, backtrack
    #                 for _ in range(steps):
    #                     curr_number //= 10
    #                 predecessor.right = None
    #                 root = root.right

    #         # If there is no left child
    #         # then just go right.
    #         else:
    #             curr_number = curr_number * 10 + root.val
    #             # if you're on the leaf, update the sum
    #             if root.right is None:
    #                 root_to_leaf += curr_number
    #             root = root.right

    #     return root_to_leaf
        
# @lc code=end

