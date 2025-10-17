#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
from collections import Counter
class Solution:
    # def findTheDifference(self, s: str, t: str) -> str:
    #     """ Approach 1: Sorting O(n log n), O(n) """

    #     # Sort both the strings
    #     sorted_s = sorted(s)
    #     sorted_t = sorted(t)

    #     # Character by character comparison
    #     i = 0
    #     while i < len(s):
    #         if sorted_s[i] != sorted_t[i]:
    #             return sorted_t[i]
    #         i += 1

    #     return sorted_t[i]
    
    
    # def findTheDifference(self, s: str, t: str) -> str:
    #     """ Approach 2: Using HashMap O(n), O(1) """
    #     # Prepare a counter for string s.
    #     # This holds the characters as keys and respective frequency as value.
    #     counter_s = Counter(s)

    #     # Iterate through string t and find the character which is not in s.
    #     for ch in t:
    #         if ch not in counter_s or counter_s[ch] == 0:
    #             return ch
    #         else:
    #             # Once a match is found we reduce frequency left.
    #             # This eliminates the possibility of a false match later.
    #             counter_s[ch] -= 1

    def findTheDifference(self, s: str, t: str) -> str:
        """ Approach 3: Bit Manipulation O(n), O(1) """

        # Initialize ch with 0, because 0 ^ X = X
        # 0 when XORed with any bit would not change the bits value.
        ch = 0

        # XOR all the characters of both s and t.
        for char_ in s:
            ch ^= ord(char_)

        for char_ in t:
            ch ^= ord(char_)

        # What is left after XORing everything is the difference.
        return chr(ch)
        
# @lc code=end

