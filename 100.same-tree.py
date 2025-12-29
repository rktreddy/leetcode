#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     """ Approach 1: Recursion O(N), O(N) """
    #     # p and q are both None
    #     if not p and not q:
    #         return True
    #     # one of p and q is None
    #     if not q or not p:
    #         return False
    #     if p.val != q.val:
    #         return False
    #     return self.isSameTree(p.right, q.right) and self.isSameTree(
    #         p.left, q.left
    #     )
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ practiece: Approach 1: Recursion O(N), O(N) """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
    # from collections import deque
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     """ Approach 2: Iteration O(N), O(N) """
    #     def check(p: TreeNode, q: TreeNode) -> bool:
    #         # if both are None
    #         if not p and not q:
    #             return True
    #         # one of p and q is None
    #         if not q or not p:
    #             return False
    #         if p.val != q.val:
    #             return False
    #         return True

    #     deq = deque(
    #         [
    #             (p, q),
    #         ]
    #     )
    #     while deq:
    #         p, q = deq.popleft()
    #         if not check(p, q):
    #             return False

    #         if p:
    #             deq.append((p.left, q.left))
    #             deq.append((p.right, q.right))

    #     return True
    
# @lc code=end

