#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # DFS
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     if None in [root.left, root.right]:
    #         return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    #     else:
    #         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
    # BFS O(n), O(n)
    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     queue = collections.deque([(root, 1)])
    #     while queue:
    #         node, level = queue.popleft()
    #         if node:
    #             if not node.left and not node.right:
    #                 return level
    #             else:
    #                 queue.append((node.left, level+1))
    #                 queue.append((node.right, level+1))

    #  def minDepth(self, root: Optional[TreeNode]) -> int:
    #       """ cracking FAANG DFS recursive O(n), O(n) """
    #       if not root:
    #            return 0
    #       self.min_depth = float('inf')
    #       self.dfs(root, 0)
    #       return self.min_depth
     
    #  def dfs(self, node, cur_depth):
    #       if not node:
    #            return
    #       if not node.left and not node.right:
    #            self.min_depth = min(self.min_depth, cur_depth + 1)
            
    #       self.dfs(node.left, cur_depth + 1)
    #       self.dfs(node.right, cur_depth + 1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """ DFS iterative O(n), O(n) """
        if not root:
            return 0
        min_depth = float('inf')
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node:
                if not node.left and not node.right:
                    min_depth = min(min_depth, depth + 1)
                else:
                    stack.append((node.left, depth + 1))
                    stack.append((node.right, depth + 1))
        return min_depth
    

# @lc code=end

