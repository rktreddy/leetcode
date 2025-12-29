#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    #     """ crack Faang: DFS with memoization O(2^N + N^2), O(2^N + N^2) """
    #     memo = {}
    #     def dfs(string):
    #         if string in memo:
    #             return memo[string]
            
    #         if not string:
    #             return [""]
            
    #         local_res = []
    #         for word in wordDict:
    #             if string.startswith(word):
    #                 sub_words = dfs(string[len(word):])

    #                 for sub_word in sub_words:
    #                     local_res.append(word + (" " if sub_word else "") + sub_word)

    #         memo[string] = local_res
    #         return local_res
        
    #     return dfs(s)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """ practice: crack Faang: DFS with memoization O(2^N + N^2), O(2^N + N^2) """
        memo = {}
        def dfs(string):
            if string in memo:
                return memo[string]
            if not string:
                return [""]
            
            local_res = []
            for word in wordDict:
                if string.startswith(word):
                    sub_words = dfs(string[len(word):])
                
                    for sub_word in sub_words:
                        local_res.append(word + (" " if sub_word else "") + sub_word)

            memo[string] = local_res
            return local_res

        return dfs(s)

        
# @lc code=end

