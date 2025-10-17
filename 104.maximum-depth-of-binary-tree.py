#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ Approach 1: Recursion O(N), O(log N)"""
        # if root is None:
        #     return 0
        # else:
        #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        
        """ Approach 2: Tail Recursion + BFS """
    # def __init__(self):
    #     # The queue that contains the next nodes to visit,
    #     # along with the level/depth that each node is located.
    #     self.next_items = []
    #     self.max_depth = 0

    # def next_maxDepth(self):
    #     if not self.next_items:
    #         return self.max_depth
    #     next_node, next_level = self.next_items.pop(0)
    #     next_level += 1
    #     self.max_depth = max(self.max_depth, next_level)
    #     # Add the nodes to visit in the following recursive calls.
    #     if next_node.left:
    #         self.next_items.append((next_node.left, next_level))
    #     if next_node.right:
    #         self.next_items.append((next_node.right, next_level))
    #     # The last action should be the ONLY recursive call
    #     # in the tail-recursion function.
    #     return self.next_maxDepth()

    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     # Clear the previous queue.
    #     self.next_items = []
    #     self.max_depth = 0
    #     # Push the root node into the queue to kick off the next visit.
    #     self.next_items.append((root, 0))
    #     return self.next_maxDepth()


    # # """ Approach 3: Iteration O(N), O(log N)"""
    # def maxDepth(self, root: TreeNode) -> int:
    #     stack = []
    #     if root is not None:
    #         stack.append((1, root))

    #     depth = 0
    #     while stack != []:
    #         current_depth, root = stack.pop()
    #         if root is not None:
    #             depth = max(depth, current_depth)
    #             stack.append((current_depth + 1, root.left))
    #             stack.append((current_depth + 1, root.right))

    #     return depth
                

# @lc code=end

