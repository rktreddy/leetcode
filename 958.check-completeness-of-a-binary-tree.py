#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    #     """ crackinng faang: BFS O(N), O(N) """
    #     null_seen = False
    #     queue = collections.deque([root])
    #     while queue:
    #         if null_seen:
    #             return not any(queue)
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             if not node:
    #                 null_seen = True
    #             else:
    #                 if null_seen:
    #                     return False
    #                 else:
    #                     queue.append(node.left)
    #                     queue.append(node.right)
    #     return True

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """ practice: crackinng faang: BFS O(N), O(N) """
        null_seen = False
        queue = collections.deque([root])
        while queue:
            if null_seen:
                return not any(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    null_seen = True
                else:
                    if null_seen:
                        return False
                    else:
                        queue.append(node.left)
                        queue.append(node.right)
        return True
        
# @lc code=end

