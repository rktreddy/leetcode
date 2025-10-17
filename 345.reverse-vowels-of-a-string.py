#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    # def reverseVowels(self, s: str) -> str:
    #     """ my initial trial """
    #     i, j = 0, len(s) - 1
    #     while i < j:
    #         while not s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
    #             i += 1
    #         while not s[j].lower() in ['a', 'e', 'i', 'o', 'u']:
    #             j -= 1
    #         s[i], s[j] = s[j], s[i]
    #         i += 1
    #         j -= 1
    #     return s
    
    # def reverseVowels(self, s: str) -> str:
    #     """ Approach 1: Two Pointers O(n), O(n) """
    #     i, j = 0, len(s) - 1
    #     listS = list(s)
    #     while i < j:
    #         while i < len(s) - 1 and not listS[i].lower() in ['a', 'e', 'i', 'o', 'u']:
    #             i += 1
    #         while j >= 0 and not listS[j] in ['a', 'e', 'i', 'o', 'u']:
    #             j -= 1
    #         if i < j:
    #             listS[i], listS[j] = listS[j], listS[i]
    #             i += 1
    #             j -= 1
                
    #     return ''.join(listS)
    
    def reverseVowels(self, s: str) -> str:
        """ Approach 1: Two Pointers O(n), O(n) chatgpt"""
        vowels = set('aeiouAEIOU')
        i, j = 0, len(s) - 1
        listS = list(s)
        
        while i < j:
            while i < j and listS[i] not in vowels:
                i += 1
            while i < j and listS[j] not in vowels:
                j -= 1
            if i < j:
                listS[i], listS[j] = listS[j], listS[i]
                i += 1
                j -= 1
                
        return ''.join(listS)

        
# @lc code=end

