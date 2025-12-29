#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    #     """ Approach 1: Preorder Traversal: Always Choose Left Middle Node as a Root O(N), O(log N) """
    #     def helper(left, right):
    #         if left > right:
    #             return None

    #         # always choose left middle node as a root
    #         p = (left + right) // 2

    #         # preorder traversal: node -> left -> right
    #         root = TreeNode(nums[p])
    #         root.left = helper(left, p - 1)
    #         root.right = helper(p + 1, right)
    #         return root

    #     return helper(0, len(nums) - 1)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """ Practice: Approach 1: Preorder Traversal: Always Choose Left Middle Node as a Root O(N), O(log N) """
        def helper(left, right):
            if left > right:
                return None
            p = (left + right) // 2
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        return helper(0, len(nums) - 1)
        
    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    #     """ Approach 2: Preorder Traversal: Always Choose Right Middle Node as a Root O(N), O(log N) """
    #     def helper(left, right):
    #         if left > right:
    #             return None

    #         # always choose right middle node as a root
    #         p = (left + right) // 2
    #         if (left + right) % 2:
    #             p += 1

    #         # preorder traversal: node -> left -> right
    #         root = TreeNode(nums[p])
    #         root.left = helper(left, p - 1)
    #         root.right = helper(p + 1, right)
    #         return root

    #     return helper(0, len(nums) - 1)
# @lc code=end

