#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     """ Approach 1: Depth-first Search O(N), O(N) """

    #     diameter = 0

    #     def longest_path(node):
    #         if not node:
    #             return 0
            
    #         nonlocal diameter

    #         left_path = longest_path(node.left)
    #         right_path = longest_path(node.right)

    #         diameter = max(diameter, left_path + right_path)

    #         return max(left_path, right_path) + 1
        
    #     longest_path(root)
    #     return diameter
    
#     # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#     #     """ for pracice"""

# class Solution:
    # def __init__(self) -> None:
    #     self.diameter = 0

    # def depth(self, node):
    #     if not node:
    #         return 0
        
    #     # left = self.depth(node.left) if node.left else 0
    #     # right = self.depth(node.right) if node.right else 0

    #     left = self.depth(node.left)
    #     right = self.depth(node.right)

    #     self.diameter = max(self.diameter, left + right)

    #     return 1 + max(right,  left)

    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     self.depth(root)
    #     return self.diameter

    # # practice
    # def __init__(self) -> None:
    #     self.diameter = 0

    # def depth(self, node):
    #     if not node:
    #         return 0
        
    #     left = self.depth(node.left)
    #     right = self.depth(node.right)

    #     self.diameter = max(self.diameter, left + right)

    #     return 1 + max(left, right)
        

    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     self.depth(root)
    #     return self.diameter
        
    # # practice 
    # def __init__(self) -> None:
    #     self.diameter = 0

    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     def depth(node):
    #         if not node:
    #             return 0
            
    #         left = depth(node.left)
    #         right = depth(node.right)

    #         self.diameter = max(self.diameter, left + right)

    #         return 1 + max(left, right)
        
    #     depth(root)
    #     return self.diameter

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
    
    # practice
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return diameter


    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     """ Neetcode DFS recursive O(N), O(N) """
    #     res = 0
    #     def dfs(root):
    #         nonlocal res 

    #         if not root:
    #             return 0
    #         left = dfs(root.left)
    #         right = dfs(root.right)

    #         res = max(res, left + right)

    #         return 1 + max(left, right) 
        
    #     dfs(root)
    #     return res 
    
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     """ Neetcode DFS iterative O(N), O(N) """
    #     stack = [root]
    #     mp = {None: (0, 0)}
    #     while stack:
    #         node = stack[-1]

    #         if node.left and node.left not in mp:
    #             stack.append(node.left)
    #         elif node.right and node.right not in mp:
    #             stack.append(node.right)
    #         else:
    #             node = stack.pop()

    #             leftHeight, leftDiameter = mp[node.left]
    #             rightHeight, rightDiameter = mp[node.right]

    #             mp[node] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))
    #     return mp[root][1]


    
# @lc code=end

# node: 4, depth: 1, dia: 0
# ' +
#   'node: 5, depth: 1, dia: 0
# ' +
#   'node: 2, depth: 2, dia: 2
# ' +
#   'node: 3, depth: 1, dia: 2
# ' +
#   'node: 1, depth: 3, dia: 3