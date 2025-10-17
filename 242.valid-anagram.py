#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
        
    #     smap = {}
    #     tmap = {}
    #     for i in range(len(s)):
    #         smap[s[i]] = smap.get(s[i], 0) + 1
    #         tmap[t[i]] = tmap.get(t[i], 0) + 1

    #     return smap == tmap
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0]*26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        return True

        
# @lc code=end

