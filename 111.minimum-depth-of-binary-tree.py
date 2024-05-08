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
        
    # BFS
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))

# @lc code=end

