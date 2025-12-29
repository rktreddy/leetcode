#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    #     if root == None:
    #          return 0
    #     if root.val > high: 
    #         return self.rangeSumBST(root.left, low, high)
    #     if root.val < low:
    #         return self.rangeSumBST(root.right, low, high)
    #     return root.val + self.rangeSumBST(root.left, low, high) \
    #                     + self.rangeSumBST(root.right, low, high)

    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    #     """ Approach 1: Depth First Search (recursive) O(N), O(N) """
    #     def dfs(node):
    #         nonlocal ans
    #         if node:
    #             if low <= node.val <= high:
    #                 ans += node.val
    #             if low < node.val:
    #                 dfs(node.left)
    #             if node.val < high:
    #                 dfs(node.right)

    #     ans = 0
    #     dfs(root)
    #     return ans

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """ Approach 1: Depth First Search (iterative) O(N), O(N) """
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans 
    
# @lc code=end

# def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    #     """ pratice; Approach 1: Depth First Search (iterative) O(N), O(N) """
    #     ans = 0
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             if low <= node.val <= high:
    #                 ans += node.val
    #         if low < node.val:
    #             stack.append(node.left)
    #         if node.val < high:
    #             stack.append(node.right)
    #     return ans

    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    #     """ Neetcode solution O(N), O(N) """
    #     if not root:
    #         return 0
    #     if root.val > high:
    #         return self.rangeSumBST(root.left, low, high)
    #     if root.val < low:
    #         return self.rangeSumBST(root.right, low, high)
    #     return root.val + self.rangeSumBST(root.left, low, high) + \
    #                         self.rangeSumBST(root.right, low, high)\
                            
    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    #     """ practice: Neetcode solution O(N), O(N) """
    #     if not root:
    #         return 0
    #     if root.val > high:
    #         return self.rangeSumBST(root.left, low, high)
    #     if root.val < low:
    #         return self.rangeSumBST(root.right, low, high)
    #     return root.val + self.rangeSumBST(root.left, low, high) \
    #                     + self.rangeSumBST(root.right, low, high)