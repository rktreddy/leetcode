#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     """ Approach 1: Two Pointers O(m + n), O(1)"""
    #     m = len(word1)
    #     n = len(word2)
    #     i = 0
    #     j = 0
    #     result = []
    #     while i < m or j < n:
    #         if i < m:
    #             result += word1[i]
    #             i += 1
    #         if j < n:
    #             result += word2[j]
    #             j += 1
    #     return "".join(result)
    
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     """ Approach 2: One Pointer O(m + n), O(1)"""
    #     result = []
    #     n = max(len(word1), len(word2))

    #     for i in range(n):
    #         if i < len(word1):
    #             result += word1[i]
    #         if i < len(word2):
    #             result += word2[i]
    #     return "".join(result)
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """ practice: Approach 2: One Pointer O(m + n), O(1) """
        result = []
        n = max(len(word1), len(word2))

        for i in range(n):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return "".join(result)

        
# @lc code=end

