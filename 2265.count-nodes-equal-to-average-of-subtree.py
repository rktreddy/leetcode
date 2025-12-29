#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def averageOfSubtree(self, root: TreeNode) -> int:
    #     """ cracking faang: DFS T:O(), S;O() """
    #     if not root:
    #         return 0
        
    #     self.average_count = 0
    #     self.dfs(root)
    #     return self.average_count
    
    # def dfs(self, node):
    #     if not node:
    #         return (0, 0)
        
    #     if not node.left and not node.right:
    #         self.average_count += 1
    #         return (node.val, 1)
        
    #     left_sum, left_count = self.dfs(node.left)
    #     right_sum, right_count = self.dfs(node.right)

    #     cur_avg = (left_sum + right_sum + node.val) // (left_count + right_count + 1)

    #     if cur_avg == node.val:
    #         self.average_count += 1

    #     return (
    #         left_sum + right_sum + node.val, 
    #         left_count + right_count + 1
    #     )

    def averageOfSubtree(self, root: TreeNode) -> int:
        """ practice: cracking faang: DFS T:O(), S;O() """
        if not root:
            return 0
        self.average_count = 0
        self.dfs(root)
        return self.average_count
    
    def dfs(self, node):
        if not node:
            return (0, 0) # sum, count
        if not node.left and not node.right:
            self.average_count += 1
            return (node.val, 1)
        left_sum, left_count = self.dfs(node.left)
        right_sum, right_count = self.dfs(node.right)

        cur_avg = (left_sum + right_sum + node.val) // (left_count + right_count + 1)

        if cur_avg == node.val:
            self.average_count += 1

        return (left_sum + right_sum + node.val, left_count + right_count + 1)
        
# @lc code=end

