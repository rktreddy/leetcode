#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if root:
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #         return root

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     """ Practice """
    #     if root:
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #         return root

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             node.left, node.right = node.right, node.left
    #             stack += node.left, node.right
    #     return root

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             node.left, node.right = node.right, node.left
    #             stack.append(node.left)
    #             stack.append(node.right)

    #     return root

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     """ practice """
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             node.left, node.right = node.right, node.left
    #             stack.append(node.left)
    #             stack.append(node.right)
    #     return root

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     """ Approach 1: Recursive O(n)", O(h) """    
        
    #     if not root:
    #         return None
        
    #     right = self.invertTree(root.right)
    #     left = self.invertTree(root.left)
    #     root.left = right
    #     root.right = left
    #     return root    

    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     """ Approach 2: Iterative O(n), O(n) """
    #     if not root:
    #         return None
        
    #     queue = collections.deque([root])
    #     while queue:
    #         current = queue.popleft()
    #         current.left, current.right = current.right, current.left
            
    #         if current.left:
    #             queue.append(current.left)
            
    #         if current.right:
    #             queue.append(current.right)
        
    #     return root

     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ pratcie: Approach 2: Iterative O(n), O(n) """
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

# @lc code=end

