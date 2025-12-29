#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """ Approach 1: Recursion O(N), O(N) """
    #     levels = []
    #     if not root:
    #         return levels
        
    #     def helper(node, level):
    #         if len(levels) == level:
    #             levels.append([])
    #         levels[level].append(node.val)
    #         if node.left:
    #             helper(node.left, level + 1)
    #         if node.right:
    #             helper(node.right, level + 1)
        
    #     helper(root, 0)

    #     return levels

    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """ practice: Approach 1: Recursion O(N), O(N) """
    #     levels = []
    #     if not root:
    #         return levels 
        
    #     def helper(node, level):
    #         if len(levels) == level:
    #             levels.append([])
    #         levels[level].append(node.val)
    #         if node.left:
    #             helper(node.left, level + 1)
    #         if node.right:
    #             helper(node.right, level + 1)

    #     helper(root, 0)
    #     return levels 
    
    # from collections import deque
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:    
    #     """ Approach 2: Iteration O(N), O(N) """
    #     levels = []
    #     if not root:
    #         return levels
        
    #     level = 0
    #     queue = deque(
    #         [
    #             root
    #         ]
    #     )

    #     while queue:
    #         levels.append([])

    #         level_length = len(queue)

    #         for i in range(level_length):
    #             node = queue.popleft()

    #             levels[level].append(node.val)

    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)

    #         level += 1

    #     return levels

    from collections import deque
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:    
    #     """ practice: Approach 2: Iteration O(N), O(N) """
    #     levels = []
    #     if not root:
    #         return levels
    #     level = 0
    #     queue = deque([root])
    #     while queue:
    #         levels.append([])
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             levels[level].append(node.val)

    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         level += 1

    #     return levels
                
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:    
        """ cracking faang: Approach 2: Iteration O(N), O(N) """
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level_items = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_items.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_items)
        return res



    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
    #     """ Top voted on leetcode """
    #     if not root:
    #         return []
        
    #     ans, level = [], [root]
    #     while level:
    #         ans.append([node.val for node in level])
    #         temp = []
    #         for node in level:
    #             temp.extend([node.left, node.right])
    #         level = [leaf for leaf in temp if leaf]
    #     return ans
        
# @lc code=end

