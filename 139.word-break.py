#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.is_node = False
        self.children = {}

class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     """ Approach 1: Breadth-First Search O(n^3 + m k), (n + m k)"""
    #     words = set(wordDict)
    #     queue = deque([0])
    #     seen = set()

    #     while queue:
    #         start = queue.popleft()
    #         if start == len(s):
    #             return True
            
    #         for end in range(start + 1, len(s) + 1):
    #             if end in seen:
    #                 continue

    #             if s[start:end] in words:
    #                 queue.append(end)
    #                 seen.add(end)

    #     return False

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     """ Approach 2: Top-Down Dynamic Programming O(n m k), O(n) """
    #     @cache 
    #     def dp(i):
    #         if i < 0:
    #             return True
            
    #         for word in wordDict:
    #             if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
    #                 return True
            
    #         return False
    #     return dp(len(s) - 1)

    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     """ Approach 3: Bottom-Up Dynamic Programming O(n m k), O(n) """
    #     dp = [False] * len(s)
    #     for i in range(len(s)):
    #         for word in wordDict:
    #             # Handle out of bounds case
    #             if i < len(word) - 1:
    #                 continue

    #             if i == len(word) - 1 or dp[i - len(word)]:
    #                 if s[i - len(word) + 1 : i + 1] == word:
    #                     dp[i] = True
    #                     break

    #     return dp[-1]
    
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """ Approach 4: Trie Optimization (n^2 + m k), O(n + m k) """
        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

            curr.is_node = True

        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]:
                curr = root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in curr.children:
                        break

                    curr = curr.children[c]
                    if curr.is_node:
                        dp[j] = True
        return dp[-1]




# @lc code=end

