#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    #     """ DFS O(n), O(n) """
    #     """
    #     Determines if there are two elements in the BST such that their sum is equal to a given target.

    #     :param root: Root node of the binary search tree
    #     :param k: Target sum we want to find
    #     :return: True if such a pair is found, False otherwise
    #     """

    #     # Helper function to perform a depth-first search
    #     def depth_first_search(node):
    #         # Base case: if the node is None, return False
    #         if node is None:
    #             return False
    #         # If the complement of the current node's value (k - node.val) is in the visited set,
    #         # we've found a pair that sums up to k.
    #         if k - node.val in visited:
    #             return True
    #         # Add the current node's value to the visited set
    #         visited.add(node.val)
    #         # Recursively search the left and right subtrees
    #         return depth_first_search(node.left) or depth_first_search(node.right)

    #     visited = set()  # Initialize an empty set to store visited node values
    #     return depth_first_search(root)  # Begin DFS with the root node

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """ DFS O(n), O(n) """
        def dfs(node):
            if not node:
                return False
            
            if k - node.val in visited:
                return True
            visited.add(node.val)

            return dfs(node.left) or dfs(node.right)
            
        visited = set()
        return dfs(root)

# @lc code=end

