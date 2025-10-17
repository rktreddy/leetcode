#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     """ Approach 1: Recursive Approach O(n), O(n) """
    #     res = []
    #     self.helper(root, res)
    #     return res 
    
    # def helper(self, root, res):
    #     if root is not None:
    #         self.helper(root.left, res)
    #         res.append(root.val)
    #         self.helper(root.right, res)

    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     """ Approach 2: Iterating method using Stack O(n), O(n) """
    #     res = []
    #     stack = []
    #     curr = root
    #     while curr or stack:
    #         while curr:
    #             stack.append(curr)
    #             curr = curr.left
    #         curr = stack.pop()
    #         res.append(curr.val)
    #         curr = curr.right
    #     return res 
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ Approach 3: Morris Traversal O(n), O(1) """
        res = []
        curr = root

        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right  # move to next right node
            else:
                pre = curr.left 
                while pre.right is not None and pre.right != curr:  # find rightmost
                    pre = pre.right
                
                if pre.right is None:
                    # establish a link back to the current node
                    pre.right = curr
                    curr = curr.left
                else:
                    # restore the tree structure
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right

        return res 
        
# @lc code=end

