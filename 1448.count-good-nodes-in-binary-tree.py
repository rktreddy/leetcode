#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def goodNodes(self, root: TreeNode) -> int:
    #     """ 1. Depth First Search O(n), O(n) """
    #     def dfs(node, maxVal):
    #         if not node:
    #             return 0

    #         res = 1 if node.val >= maxVal else 0
    #         maxVal = max(maxVal, node.val)
    #         res += dfs(node.left, maxVal)
    #         res += dfs(node.right, maxVal)
    #         return res

    #     return dfs(root, root.val)

    def goodNodes(self, root: TreeNode) -> int:
        """ pracice: 1. Depth First Search O(n), O(n) """
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        return dfs(root, root.val)
    
    # def goodNodes(self, root: TreeNode) -> int:
    #     """ 2. Breadth First Search O(n), O(n) """
    #     res = 0
    #     q = deque()

    #     q.append((root,-float('inf')))

    #     while q:
    #         node,maxval = q.popleft()
    #         if node.val >= maxval:
    #             res += 1

    #         if node.left:
    #             q.append((node.left,max(maxval,node.val)))

    #         if node.right:
    #             q.append((node.right,max(maxval,node.val)))

    #     return res
    
    # def goodNodes(self, root: TreeNode) -> int:
    #     """ practice: 2. Breadth First Search O(n), O(n) """
    #     res = 0
    #     queue = deque([(root, root.val)])
    #     while queue:
    #         node, maxVal = queue.popleft()
    #         if node.val >= maxVal:
    #             res += 1
    #         maxVal = max(maxVal, node.val)
    #         if node.left:
    #             queue.append((node.left, maxVal))
    #         if node.right:
    #             queue.append((node.right, maxVal))
    #     return res
        
# @lc code=end

