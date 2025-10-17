#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    # """ Original implementatio """
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     charSet = set()
    #     l = 0

    #     res = 0
    #     for r in range(len(s)):
    #         while s[r] in charSet:
    #             charSet.remove(s[l])
    #             l += 1
    #         charSet.add(s[r])
    #         res = max(res, r - l + 1)
    #     return res
    
    # def lengthOfLongestSubstring(self, s: str) -> int:
        # """ Approach 1: Brute Force O(n^3), O(min(n, m)) """
    #     def check(start, end):
    #         chars = set()
    #         for i in range(start, end + 1):
    #             c = s[i]
    #             if c in chars:
    #                 return False
    #             chars.add(c)
    #         return True

    #     n = len(s)

    #     res = 0
    #     for i in range(n):
    #         for j in range(i, n):
    #             if check(i, j):
    #                 res = max(res, j - i + 1)
    #     return res
    
    # from collections import Counter

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """ Approach 2: Sliding Window O(n), O(min(n, m))"""

    #     chars = Counter()

    #     left = right = 0

    #     res = 0
    #     while right < len(s):
    #         r = s[right]
    #         chars[r] += 1

    #         while chars[r] > 1:
    #             l = s[left]
    #             chars[l] -= 1
    #             left += 1

    #         res = max(res, right - left + 1)

    #         right += 1
    #     return res

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """ Approach 3: Sliding Window Optimized O(n), O(min(n, m)) """
    #     n = len(s)
    #     ans = 0
    #     mp = {}

    #     i = 0
    #     for j in range(n):
    #         if s[j] in mp:
    #             i = max(mp[s[j]], i)
            
    #         ans = max(ans, j - i + 1)
    #         mp[s[j]] = j + 1
        
    #     return ans

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """ neetcode: sliding window optimal O(n), O(m) """
    #     mp = {}
    #     l = 0
    #     res = 0
        
    #     for r in range(len(s)):
    #         if s[r] in mp:
    #             l = max(mp[s[r]] + 1, l)
    #         mp[s[r]] = r
    #         res = max(res, r - l + 1)
    #     return res
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ practice: neetcode: sliding window optimal O(n), O(m) """
        mp = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """ Top upvoted solution on leetcode"""
    #     seen = {}
    #     l = 0
    #     output = 0
    #     for r in range(len(s)):
    #         if s[r] not in seen:
    #             output = max(output, r-l+1)
    #         else:
    #             if seen[s[r]] < l:
    #                 output = max(output, r-l+1)
    #             else:
    #                 l = seen[s[r]] + 1
    #         seen[s[r]] = r
    #     return output

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """ Neetcode solution O(n), O(n) """
    #     charSet = set()
    #     l = 0
    #     res = 0

    #     for r in range(len(s)):
    #         while s[r] in charSet:
    #             charSet.remove(s[l])
    #             l += 1
    #         charSet.add(s[r])
    #         res = max(res, r - l + 1)
    #     return res


    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     """ pratcice: sliding window O(n), O(n) """
    #     charSet = set()
    #     res = 0
    #     l = 0
    #     for r in range(len(s)):
    #         while s[r] in charSet:
    #             charSet.remove(s[l])
    #             l += 1
    #         charSet.add(s[r])
    #         res = max(res, r - l + 1)
    #     return res

# @lc code=end

