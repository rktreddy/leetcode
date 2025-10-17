#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """ bfs?, O(N), O(M), M is max modes at a level"""
        # Initialize a queue for breadth-first traversal with the root node
        queue = deque([root])
        # List to store the averages of each level
        averages = []
      
        # Loop while there are nodes in the queue
        while queue:
            # Initialize the sum and get the number of nodes at the current level
            level_sum, num_nodes = 0, len(queue)
            # Iterate over all nodes at the current level
            for _ in range(num_nodes):
                # Pop the first node from the queue
                node = queue.popleft()
                # Add its value to the level sum
                level_sum += node.val
                # If there is a left child, add it to the queue
                if node.left:
                    queue.append(node.left)
                # If there is a right child, add it to the queue
                if node.right:
                    queue.append(node.right)
            # Calculate the average for the level and add it to the result list
            averages.append(level_sum / num_nodes)
          
        return averages
        
# @lc code=end

