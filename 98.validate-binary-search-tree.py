#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     """ Approach 1: Recursive Traversal with Valid Range O(N), O(N) """

    #     def validate(node, low = -math.inf, high = math.inf):
    #         if not node:
    #             return True
            
    #         if node.val <= low or node.val >= high:
    #             return False
            
    #         return validate(node.left, low, node.val) and validate(
    #             node.right, node.val, high)
        
    #     return validate(root)

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     """ Approach 2: Iterative Traversal with Valid Range O(N), O(N) """
            
    #     if not root:
    #         return True
        
    #     stack = [(root, -math.inf, math.inf)]

    #     while stack:
    #         root, low, high = stack.pop()
            
    #         if not root:
    #             continue
            
    #         if root.val <= low or root.val >= high:
    #             return False

    #         stack.append([root.left, low, root.val])
    #         stack.append([root.right, root.val, high])

    #     return True
    
    
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     """ Approach 3: Recursive Inorder Traversal O(N), O(N) """

    #     def inorder(root):
    #         if not root:
    #             return True
    #         if not inorder(root.left):
    #             return False
    #         if root.val <= self.prev:
    #             return False
    #         self.prev = root.val
    #         return inorder(root.right)
        
    #     self.prev = -math.inf
    #     return inorder(root)

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     """ Approach 4: Iterative Inorder Traversal O(N), O(N) """
    #     stack, prev = [], -math.inf

    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()

    #         # If next element in inorder traversal
    #         # is smaller than the previous one
    #         # that's not BST.
    #         if root.val <= prev:
    #             return False
    #         prev = root.val
    #         root = root.right

    #     return True
    
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     """ practice: Approach 4: Iterative Inorder Traversal O(N), O(N) """
    #     stack = []
    #     prev = float("-inf")
    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()
    #         if root.val <= prev:
    #             return False
    #         prev = root.val
    #         root = root.right
    #     return True
    

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     """ Neetcode: Recursive DFS O(n), O(n) """
    #     def valid(node, left, right):
    #         if not node:
    #             return True
    #         if not (left < node.val < right):
    #             return False

    #         return valid(node.left, left, node.val) and valid(
    #             node.right, node.val, right
    #         )

    #     return valid(root, float("-inf"), float("inf"))
    
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     """ cracking faang: Recursive DFS O(n), O(n) """

    
# @lc code=end

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """ practice: Approach 2: Iterative Traversal with Valid Range O(N), O(N) """
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))] # root, low, high
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if node.val <= low or node.val >= high:
                return False
            stack.append(node.left, low, node.val)
            stack.append(node.right, node.val, high)
        return True