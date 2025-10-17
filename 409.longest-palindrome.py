#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    """ Approach 1: Greedy Way (Hash Table): T O(n), S O(1) """
    # def longestPalindrome(self, s: str) -> int:
    #     frequency_map = {}
    #     for c in s:
    #         frequency_map[c] = frequency_map.get(c, 0) + 1

    #     res = 0
    #     hasOddfreq = False

    #     for freq in frequency_map.values():
    #         if freq % 2 == 0:
    #             res += freq
    #         else:
    #             res += freq - 1
    #             hasOddfreq = True
    #     return res + 1 if hasOddfreq else res

    """ Approach 2: Greedy Way (Optimized): T O(n), S O(1)  """
    # def longestPalindrome(self, s: str) -> int:
    #     oddFreqlen = 0
    #     frequence_map = {}
    #     for c in s:
    #         frequence_map[c] = frequence_map.get(c, 0) + 1

    #         if frequence_map[c] % 2 == 1:
    #             oddFreqlen += 1
    #         else:
    #             oddFreqlen -= 1

    #     if oddFreqlen > 0:
    #         return len(s) - oddFreqlen + 1
    #     else:
    #         return len(s)
        
    """ Approach 3: Greedy Way (Hash Set): T O(n), S O(1) """
    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0

        for c in s:
            if c in character_set:
                character_set.remove(c)
                res += 2
            else:
                character_set.add(c)

        if character_set:
            res += 1
            
        return res

# @lc code=end

