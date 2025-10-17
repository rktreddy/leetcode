#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     """ Approach 1: Recursive Inorder Traversal O(N), O(N) """
    #     def inorder(r: Optional[TreeNode]) -> List[int]:
    #         return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
    #     return inorder(root)[k - 1]
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """ Approach 2: Iterative Inorder Traversal O(H + k), O(N) """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
            
        
# @lc code=end

