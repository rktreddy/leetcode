#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    #     """ Approach 1: Breadth First Search (BFS) O(n), O(n)  """
    #     if not root:
    #         return []
        
    #     ans = []
    #     queue = deque([root])
        
    #     while queue:
    #         current_length = len(queue)
    #         curr_max = float("-inf")
            
    #         for _ in range(current_length):
    #             node = queue.popleft()
    #             curr_max = max(curr_max, node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
            
    #         ans.append(curr_max)
        
    #     return ans
    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """ practice: Approach 1: Breadth First Search (BFS) O(n), O(n)  """
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            max_val = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_val)
        return res
    
    # def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    #     """ Approach 2: Depth First Search (DFS) O(n), O(h)  """
    #     def dfs(node, depth):
    #         if not node:
    #             return
            
    #         if depth == len(ans):
    #             ans.append(node.val)
    #         else:
    #             ans[depth] = max(ans[depth], node.val)
            
    #         dfs(node.left, depth + 1)
    #         dfs(node.right, depth + 1)
        
    #     ans = []
    #     dfs(root, 0)
    #     return ans
    
    

# @lc code=end

