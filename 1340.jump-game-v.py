#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#

# @lc code=start
class Solution:
    # def maxJumps(self, arr: List[int], d: int) -> int:
    #     """ cracking faang: graph:DFS + Memoization O(N*D).O(N*D) """
    #     self.graph = collections.defaultdict(set)
    #     self.memo = {}
    #     N = len(arr)
    #     for i in range(N):
    #         for j in range(i + 1, N):
    #             if arr[j] < arr[i] and abs(i - j) <= d:
    #                 self.graph[i].add(j)
    #             else:
    #                 break
        
    #         for j in range(i - 1, -1, -1):
    #             if arr[j] < arr[i] and abs(i - j) <= d:
    #                 self.graph[i].add(j)
    #             else:
    #                 break

    #     res = 0
    #     for i in range(N):
    #         res = max(res, self.dfs(i, N))

    #     return res
    
    # def dfs(self, cur_idx, N):
    #     if cur_idx == N:
    #         return 0
        
    #     if cur_idx in self.memo:
    #         return self.memo[cur_idx]
        
    #     path = 1
    #     for next_hop in self.graph[cur_idx]:
    #         path = max(path, 1 + self.dfs(next_hop, N))
        
    #     self.memo[cur_idx] = path

    #     return path
    
    # def maxJumps(self, arr: List[int], d: int) -> int:
    #     """ chatgpt: cracking faang: graph:DFS + Memoization O(N*D).O(N*D) """
        
    #     n = len(arr)
    #     graph = [[] for _ in range(n)]

    #     # Build directed graph for jumps
    #     for i in range(n):

    #         # jump right
    #         for j in range(i+1, min(n, i+d+1)):
    #             if arr[j] >= arr[i]:
    #                 break
    #             graph[i].append(j)

    #         # jump left
    #         for j in range(i-1, max(-1, i-d)-1, -1):
    #             if arr[j] >= arr[i]:
    #                 break
    #             graph[i].append(j)

    #     @functools.lru_cache(None)
    #     def dfs(i):
    #         best = 1   # at least stay here
    #         for nxt in graph[i]:
    #             best = max(best, 1 + dfs(nxt))
    #         return best

    #     return max(dfs(i) for i in range(n))
    

    def maxJumps(self, arr: List[int], d: int) -> int:
        """ practice: chatgpt: cracking faang: graph:DFS + Memoization O(N*D).O(N*D) """
        n = len(arr)
        grapth = [[] for _ in range(n)]
        for i in range(n):
            # jump right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                grapth[i].append(j)
            # jump left
            for j in range(i - 1, max(-1, i - d)-1, -1):
                if arr[j] >= arr[i]:
                    break
                grapth[i].append(j)

        @functools.lru_cache(None)
        def dfs(i):
            best = 1
            for nxt in grapth[i]:
                best = max(best, 1 + dfs(nxt))
            return best
        
        return max(dfs(i) for i in range(n))

        
# @lc code=end

# # lru_cache IS memoization, just a built-in version
# #  and is implemented in optimized C code → very fast lookup.
# 2. Automatically handles edge cases

# Hashing

# Storing keys

# Performance

# Repeated calls

# @lru_cache(None)
# def dfs(i):


# ## manual memoization
# memo = {}
# def dfs(i):
#     if i in memo:
#         return memo[i]
