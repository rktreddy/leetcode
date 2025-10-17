#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    #     """ DFS: Approach 1: Implementing Parent Pointers O(n), O(n) """
    #     # Recursively add a parent pointer to each node.
    #     def add_parent(cur, parent):
    #         if cur:
    #             cur.parent = parent
    #             add_parent(cur.left, cur)
    #             add_parent(cur.right, cur) 
    #     add_parent(root, None)
        
    #     answer = []
    #     visited = set()
    #     def dfs(cur, distance):
    #         if not cur or cur in visited:
    #             return
    #         visited.add(cur)
    #         if distance == 0:
    #             answer.append(cur.val)
    #             return
    #         dfs(cur.parent, distance - 1)
    #         dfs(cur.left, distance - 1)
    #         dfs(cur.right, distance - 1)
            
    #     dfs(target, k)
        
    #     return answer
        
    # def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    #     """ Approach 2: Depth-First Search on Equivalent Graph O(n), O(n) """
    #     graph = collections.defaultdict(list)
        
    #     # Recursively build the undirected graph from the given binary tree.
    #     def build_graph(cur, parent):
    #         if cur and parent:
    #             graph[cur.val].append(parent.val)
    #             graph[parent.val].append(cur.val)
    #         if cur.left:
    #             build_graph(cur.left, cur)
    #         if cur.right:
    #             build_graph(cur.right, cur) 
    #     build_graph(root, None)
        

    #     answer = []
    #     visited = set([target.val])
        
    #     def dfs(cur, distance):
    #         if distance == k:
    #             answer.append(cur)
    #             return
    #         for neighbor in graph[cur]:
    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 dfs(neighbor, distance + 1)
    #     dfs(target.val, 0)
        
    #     return answer
    
    # def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    #     """ Approach 3: Breadth-First Search on Equivalent Graph O(n), O(n) """
    #     graph = collections.defaultdict(list)
    #     # Recursively build the undirected graph from the given binary tree.
    #     def build_graph(cur, parent):
    #         if cur and parent:
    #             graph[cur.val].append(parent.val)
    #             graph[parent.val].append(cur.val)
    #         if cur.left:
    #             build_graph(cur.left, cur)
    #         if cur.right:
    #             build_graph(cur.right, cur) 
    #     build_graph(root, None)
        
    #     answer = []
    #     visited = set([target.val])

    #     # Add the target node to the queue with a distance of 0
    #     queue = collections.deque([(target.val, 0)])
    #     while queue:
    #         cur, distance = queue.popleft()

    #         # If the current node is at distance k from target,
    #         # add it to the answer list and continue to the next node.
    #         if distance == k:
    #             answer.append(cur)
    #             continue

    #         # Add all unvisited neighbors of the current node to the queue.
    #         for neighbor in graph[cur]:
    #             if neighbor not in visited:
    #                 visited.add(neighbor)
    #                 queue.append((neighbor, distance + 1))
                    
    #     return answer

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """practice: Approach 3: Breadth-First Search on Equivalent Graph O(n), O(n) """
        graph = collections.defaultdict(list)
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)

        build_graph(root, None)

        answer = []
        visited = set([target.val])

        queue = collections.deque([(target.val, 0)])

        while queue:
            cur, distance = queue.popleft()

            if distance == k:
                answer.append(cur)
                continue

            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
                
        return answer

# @lc code=end

