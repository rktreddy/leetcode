#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     """ cracking faang: T: O(E log V), S: O(E + V) """
    #     graph = collections.defaultdict(list)
    #     for src, dst in sorted(tickets, reverse=True):
    #         graph[src].append(dst)
    #     stack = ["JFK"]
    #     itenerary = []
    #     while stack:
    #         while graph[stack[-1]]:
    #             stack.append(graph[stack[-1]].pop())
    #         itenerary.append(stack.pop())
    #     return list(reversed(itenerary))

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """ practice: cracking faang: T: O(E log V), S: O(E + V) """
        graph = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        stack = ["JFK"]
        itinerary = []
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itinerary.append(stack.pop())
        return list(reversed(itinerary))
        
# @lc code=end

