#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isEvenOddTree(self, root: Optzional[TreeNode]) -> bool:
    #     """ Approach 1: Depth-First Search O(n), O(n) """
    #     prev = []

    #     def dfs(current: TreeNode, level: int) -> bool:
    #         # Base case, an empty tree is Even-Odd
    #         if current is None:
    #             return True

    #         # Compare the parity of current and level
    #         if current.val % 2 == level % 2:
    #             return False

    #         # Add a new level to prev if we've reached a new level
    #         while(len(prev) <= level):
    #             prev.append(0)

    #         # If there are previous nodes on this level, check increasing/decreasing
    #         # If on an even level, check that current's value is greater than the previous on this level
    #         # If on an odd level, check that current's value is less than the previous on this level
    #         if prev[level] != 0 and \
    #                 ((level % 2 == 0 and current.val <= prev[level]) or \
    #                  (level % 2 == 1 and current.val >= prev[level])):
    #             return False

    #         # Add current value to prev at index level
    #         prev[level] = current.val

    #         # Recursively call DFS on the left and right children
    #         return dfs(current.left, level + 1) and dfs(current.right, level + 1)
        
    #     current = root
    #     return dfs(current, 0)
    
    # def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
    #     """ Approach 2: Breadth-First Search O(n), O(n) """
    #     # Create a queue for nodes that need to be visited and add the root
    #     queue = deque()
    #     current = root
    #     queue.append(current)

    #     # Keeps track of whether we are on an even level
    #     even = True

    #     # While there are more nodes in the queue
    #     # Determine the size of the level and handle the nodes
    #     while queue:
    #         size = len(queue)

    #         # Prev holds the value of the previous node in this level
    #         prev = float("inf")
    #         if even:
    #             prev = -prev

    #         # While there are more nodes in this level
    #         # Remove a node, check whether it satisfies the conditions
    #         # Add its children to the queue
    #         while size > 0:
    #             current = queue.popleft()

    #             # If on an even level, check that the node's value is odd and greater than prev
    #             # If on an odd level, check that the node's value is even and less than prev
    #             if (even and (current.val % 2 == 0 or current.val <= prev)) or \
    #                     (not even and (current.val % 2 == 1 or current.val >= prev)):
    #                 return False

    #             prev = current.val
    #             if current.left:
    #                 queue.append(current.left)
    #             if current.right:
    #                 queue.append(current.right)
    #             # Decrement size, we have handled a node on this level
    #             size -= 1

    #         # Flip the value of even, the next level will be opposite
    #         even = not even

    #     # If every node meets the conditions, the tree is Even-Odd
    #     return True

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """ cracking faang: Breadth-First Search O(n), O(n) """
        if not root:
            return True
        cur_level = 0
        queue = collections.deque([root])
        while queue:
            odd_level = cur_level % 2 == 1
            prev_seen = float('inf') if odd_level else float('-inf')
            for _ in range(len(queue)):
                cur_node = queue.popleft()

                if odd_level:
                    if cur_node.val % 2 != 0 or cur_node.val >= prev_seen:
                        return False
                else:
                    if cur_node.val % 2 != 1 or cur_node.val <= prev_seen:
                        return False
                    
                prev_seen = cur_node.val
                    
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            cur_level += 1
        
        return True
    
    # def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
    #     """ chatgpt: cracking faang: Breadth-First Search O(n), O(n) """
    #     from collections import deque

    #     if not root:
    #         return True

    #     queue = deque([root])
    #     level = 0

    #     while queue:
    #         size = len(queue)
    #         prev = float('inf') if level % 2 else float('-inf')

    #         for _ in range(size):
    #             node = queue.popleft()

    #             # Even level: values must be odd and strictly increasing
    #             if level % 2 == 0:
    #                 if node.val % 2 == 0 or node.val <= prev:
    #                     return False

    #             # Odd level: values must be even and strictly decreasing
    #             else:
    #                 if node.val % 2 == 1 or node.val >= prev:
    #                     return False

    #             prev = node.val

    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)

    #         level += 1

    #     return True


        
# @lc code=end

