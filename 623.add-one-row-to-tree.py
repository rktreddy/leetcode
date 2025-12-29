#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    #     """ cracking faang: BFS O(N), O(N) """
    #     if depth == 1:
    #         return TreeNode(val, root, None)
        
    #     cur_depth = 1
    #     queue = collections.deque([root])
    #     while queue:
    #         if cur_depth == depth - 1:
    #             break
    #         for _ in range(len(queue)):
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         cur_depth += 1

    #     for node in queue:
    #         cur_left = node.left
    #         node.left = TreeNode(val, cur_left, None)

    #         cur_right = node.right
    #         node.right = TreeNode(val, None, cur_right)

    #     return root
    
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """ practice: cracking faang: BFS O(N), O(N) """
        if depth == 1:
            return TreeNode(val, root, None)
        cur_depth = 1
        queue = collections.deque([root])
        while queue:
            if cur_depth == depth - 1:
                break
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            cur_depth += 1
        for node in queue:
            cur_left = node.left
            node.left = TreeNode(val, cur_left, None)
            cur_right = node.right
            node.right = TreeNode(val, None, cur_right)
        return root


        
# @lc code=end

