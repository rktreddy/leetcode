#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     """ Approach 1: Topological Sort Using Kahn's Algorithm O(m + n), O(m + n)"""
    #     indegree = [0] * numCourses
    #     adj = [[] for _ in range(numCourses)]

    #     for prerequisite in prerequisites:
    #         adj[prerequisite[1]].append(prerequisite[0])
    #         indegree[prerequisite[0]] += 1

    #     queue = deque()
    #     for i in range(numCourses):
    #         if indegree[i] == 0:
    #             queue.append(i)

    #     nodes_visisted = 0
    #     while queue:
    #         node = queue.popleft()
    #         nodes_visisted += 1

    #         for neighbor in adj[node]:
    #             indegree[neighbor] -= 1
    #             if indegree[neighbor] == 0:
    #                 queue.append(neighbor)

    #     return nodes_visisted == numCourses

    def dfs(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True
        inStack[node] = False
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ Approach 2: Depth First Search O(m + n), O(m + n) """
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        visit = [False] * numCourses
        inStack = [False] * numCourses

        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False
        return True
        

# @lc code=end

