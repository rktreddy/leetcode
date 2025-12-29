#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """ Approach 1: BFS (Breadth-First Search) O(n), O(n) """
    #     # Definition for a binary tree node.
    #     ret = []
    #     level_list = deque()
    #     if root is None:
    #         return []
    #     # start with the level 0 with a delimiter
    #     node_queue = deque([root, None])
    #     is_order_left = True

    #     while len(node_queue) > 0:
    #         curr_node = node_queue.popleft()

    #         if curr_node:
    #             if is_order_left:
    #                 level_list.append(curr_node.val)
    #             else:
    #                 level_list.appendleft(curr_node.val)

    #             if curr_node.left:
    #                 node_queue.append(curr_node.left)
    #             if curr_node.right:
    #                 node_queue.append(curr_node.right)
    #         else:
    #             # we finish one level
    #             ret.append(list(level_list))
    #             # add a delimiter to mark the level
    #             if len(node_queue) > 0:
    #                 node_queue.append(None)

    #             # prepare for the next level
    #             level_list = deque()
    #             is_order_left = not is_order_left

    #     return ret
    
    # def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """ cracking faang: Approach 1: BFS (Breadth-First Search) O(n), O(n) """
    #     if not root:
    #         return []
    #     res = []
    #     queue = collections.deque([root])
    #     going_right = True

    #     while queue:
    #         level_items = []
    #         for _ in range(len(queue)):
    #             if going_right:
    #                 node = queue.popleft()
    #                 level_items.append(node.val)
    #                 if node.left:
    #                     queue.append(node.left)
    #                 if node.right:
    #                     queue.append(node.right)
    #             else:
    #                 node = queue.pop()
    #                 level_items.append(node.val)
    #                 if node.right:
    #                     queue.appendleft(node.right)
    #                 if node.left:
    #                     queue.appendleft(node.left)
                        
    #         res.append(level_items)
    #         going_right = not going_right
    #     return res
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ practice: cracking faang: Approach 1: BFS (Breadth-First Search) O(n), O(n) """
        if not root:
            return []
        res = []
        queue = deque([root])
        going_right = True
        while queue:
            level_items = []
            for _ in range(len(queue)):
                if going_right:
                    node = queue.popleft()
                    level_items.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    level_items.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            res.append(level_items)
            going_right = not going_right
        return res

            
    
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    #     """ Approach 2: DFS (Depth-First Search) O(n), O(n) """
    #     # Definition for a binary tree node.

    #     if root is None:
    #         return []

    #     results = []

    #     def dfs(node: TreeNode, level: int) -> None:
    #         if level >= len(results):
    #             results.append(deque([node.val]))
    #         else:
    #             if level % 2 == 0:
    #                 results[level].append(node.val)
    #             else:
    #                 results[level].appendleft(node.val)

    #         for next_node in [node.left, node.right]:
    #             if next_node is not None:
    #                 dfs(next_node, level + 1)

    #     # normal level order traversal with DFS
    #     dfs(root, 0)

    #     return results
        
# @lc code=end

