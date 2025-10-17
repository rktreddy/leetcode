#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # def __init__(self) -> None:
    #     self.visited = {}

    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     """ Approach 1: Depth First Search O(N + M), O(N)"""
    #     if not node:
    #         return node
        
    #     if node in self.visited:
    #         return self.visited[node]
        
    #     clone_node = Node(node.val, [])

    #     self.visited[node] = clone_node

    #     if node.neighbors:
    #         clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

    #     return clone_node

    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     """ Approach 2: Breadth First Search O(N + M), O(N) """
    #     if not node:
    #         return node
        
    #     visited = {}

    #     queue = deque([node])

    #     visited[node] = Node(node.val, [])

    #     while queue:
    #         n = queue.popleft()

    #         for neighbor in n.neighbors:
    #             if neighbor not in visited:
    #                 visited[neighbor] = Node(neighbor.val, [])
    #                 queue.append(neighbor)

    #             visited[n].neighbors.append(visited[neighbor])

    #     return visited[node]
    
    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     """ practice: Approach 2: Breadth First Search O(N + M), O(N), nodes and edges """
    #     if not node:
    #         return node
        
    #     queue = deque([node])
    #     visited = {}

    #     visited[node] = Node(node.val, [])

    #     while queue:
    #         n = queue.popleft()
    #         for neighbor in n.neighbors:
    #             if neighbor not in visited:
    #                 visited[neighbor] = Node(neighbor.val, [])
    #                 queue.append(neighbor)
    #             visited[n].neighbors.append(visited[neighbor])

    #     return visited[node]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """ practice: Approach 2: Breadth First Search O(N + M), O(N), nodes and edges """
        if not node:
            return node
        
        visited = {}
        visited[node] = Node(node.val, [])
        queue = deque([node])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]

# @lc code=end

