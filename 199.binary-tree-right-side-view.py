#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     """ Approach 1: BFS: Two Queues O(N), O(D), D - diameter"""
    #     if root is None:
    #         return []
        
    #     next_level = deque(
    #         [
    #             root,
    #         ]
    #     )
    #     rightside = []

    #     while next_level:
    #         curr_level = next_level
    #         next_level = deque()

    #         while curr_level:
    #             node = curr_level.popleft()
    #             if node.left:
    #                 next_level.append(node.left)
    #             if node.right:
    #                 next_level.append(node.right)

    #         rightside.append(node.val)

    #     return rightside

    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     """ Approach 2: BFS: One Queue + Sentinel O(N), O(D) """
    #     if root is None:
    #         return []
        
    #     queue = deque(
    #         [
    #             root,
    #             None,
    #         ]
    #     )
    #     rightside = []

    #     curr = root
    #     while queue:
    #         prev, curr = curr, queue.popleft()

    #         while curr:
    #             if curr.left:
    #                 queue.append(curr.left)
    #             if curr.right:
    #                 queue.append(curr.right)

    #             prev, curr = curr, queue.popleft()

    #         rightside.append(prev.val)

    #         if queue:
    #             queue.append(None)

    #     return rightside
    
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     """ Approach 3: BFS: One Queue + Level Size Measurements O(N), O(D) """
    #     if root is None:
    #         return []
        
    #     queue = deque(
    #         [
    #             root,
    #         ]
    #     )
    #     rightside = []

    #     while queue:
    #         level_length = len(queue)

    #         for i in range(level_length):
    #             node = queue.popleft()

    #             if i == level_length - 1:
    #                 rightside.append(node.val)

    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)

    #     return rightside

    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     """ Approach 4: Recursive DFS O(N), O(H), H - height """
    #     if root is None:
    #         return []
        
    #     rightside = []

    #     def helper(node: TreeNode, level: int) -> None:
    #         if level == len(rightside):
    #             rightside.append(node.val)

    #         for child in [node.right, node.left]:
    #             if child:
    #                 helper(child, level + 1)

    #     helper(root, 0)
    #     return rightside

    # def rightSideView(self, root: TreeNode | None) -> list[int]:
    #     """ BFS O(N), O(N) """
    #     if not root:
    #         return []

    #     ans = []
    #     q = collections.deque([root])

    #     while q:
    #         length = len(q)
    #         for i in range(length):
    #             root = q.popleft()
    #             if i == length - 1:
    #                 ans.append(root.val)
    #             if root.left:
    #                 q.append(root.left)
    #             if root.right:
    #                 q.append(root.right)

    #     return ans
    
    # def rightSideView(self, root: TreeNode | None) -> list[int]:
    #     """ practice: BFS O(N), O(D) D: diameter """
    #     right_side_view = []
    #     if not root:
    #         return right_side_view
    #     queue = deque([root])

    #     while queue:
    #         length = len(queue)
    #         for i in range(length):
    #             node = queue.popleft()
    #             if i == length - 1:
    #                 right_side_view.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)

    #     return right_side_view

    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """ practice: BFS O(N), O(D) D: diameter """
        right_side_view = []
        if not root:
            return right_side_view
        queue = deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if i == length - 1:
                    right_side_view.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_side_view

    # def rightSideView(self, root: TreeNode | None) -> list[int]:
    #     """ Approach 4: Recursive DFS O(N), O(H), H - height """
    #     ans = []

    #     def dfs(root: TreeNode | None, depth: int) -> None:
    #         if not root:
    #             return

    #         if depth == len(ans):
    #             ans.append(root.val)
    #         dfs(rooet.right, depth + 1)
    #         dfs(root.left, depth + 1)

    #     dfs(root, 0)
    #     return ans
    
    # def rightSideView(self, root: TreeNode | None) -> list[int]:
    #     """ practice: Approach 4: Recursive DFS O(N), O(H), H - height """
    #     ans = []
    #     def dfs(node, depth):
    #         if not node:
    #             return 
            
    #         if depth == len(ans):
    #             ans.append(node.val)
    #         dfs(node.right, depth + 1)
    #         dfs(node.left, depth + 1)

    #     dfs(root, 0)
    #     return ans
    
# @lc code=end

