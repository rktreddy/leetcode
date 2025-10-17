#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    # def countSubstrings(self, s: str) -> int:
    #     """ Top voted solution """
    #     ans, n, i = 0, len(s), 0
    #     while (i < n):
    #         j, k = i - 1, i
    #         while k < n - 1 and s[k] == s[k+1]: k += 1                
    #         ans += (k - j) * (k - j + 1) // 2
    #         i, k = k + 1, k + 1
    #         while ~j and k < n and s[k] == s[j]:
    #             j, k, ans = j - 1, k + 1, ans + 1
    #     return ans
    
    ## Neetcode solutions
    # def countSubstrings(self, s: str) -> int:
    #     """ 1. Brute Force O(n^3), O(1) """
    #     res = 0
        
    #     for i in range(len(s)):
    #         for j in range(i, len(s)):
    #             l, r = i, j
    #             while l < r and s[l] == s[r]:
    #                 l += 1
    #                 r -= 1
    #             res += (l >= r)
                
    #     return res
    
    # def countSubstrings(self, s: str) -> int:
    #     """ 2. Dynamic Programming O(n^2), O(n^2) """
    #     n, res = len(s), 0
    #     dp = [[False] * n for _ in range(n)]

    #     for i in range(n - 1, -1, -1):
    #         for j in range(i, n):
    #             if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
    #                 dp[i][j] = True
    #                 res += 1

    #     return res
    
    # def countSubstrings(self, s: str) -> int:
    #     """ 3. Two Pointers O(n^2), O(1) """
    #     res = 0
        
    #     for i in range(len(s)):
    #         # odd length
    #         l, r = i, i
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             res += 1
    #             l -= 1
    #             r += 1

    #         # even length
    #         l, r = i, i + 1
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             res += 1
    #             l -= 1
    #             r += 1
        
    #     return res

    # def countSubstrings(self, s: str) -> int:
    #     """ 4. Two Pointers (Optimal) O(n^2), O(1) """
    #     res = 0
        
    #     for i in range(len(s)):
    #         res += self.countPali(s, i, i)
    #         res += self.countPali(s, i, i + 1)
    #     return res

    # def countPali(self, s, l, r):
    #     res = 0
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         res += 1
    #         l -= 1
    #         r += 1
    #     return res

    def countSubstrings(self, s: str) -> int:
        """ practice: 4. Two Pointers (Optimal) O(n^2), O(1) """
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
        

    # def countSubstrings(self, s: str) -> int:
    #     """ 5. Manacher's Algorithm O(n), O(n) """

    #     def manacher(s):
    #         t = '#' + '#'.join(s) + '#'
    #         n = len(t)
    #         p = [0] * n
    #         l, r = 0, 0
    #         for i in range(n):
    #             p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
    #             while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]):
    #                 p[i] += 1
    #             if i + p[i] > r:
    #                 l, r = i - p[i], i + p[i]
    #         return p
        
    #     p = manacher(s)
    #     res = 0
    #     for i in p:
    #         res += (i + 1) // 2
    #     return res
    

    # def countSubstrings(self, s: str) -> int:
    #     """ practice: 5. Manacher's Algorithm O(n), O(n) """

    #     def manacher(s):
    #         t = '#' + '#'.join(s) + '#'
    #         n = len(t)
    #         p = [0] * n
    #         l, r = 0, 0
    #         for i in range(n):
    #             p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
    #             while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 
    #                    and t[i + p[i] + 1] == t[i - p[i] - 1]):
    #                 p[i] += 1
    #             if i + p[i] > r:
    #                 l, r = i - p[i], i + p[i]
    #         return p
        
    #     p = manacher(s)
    #     res = 0
    #     for i in p:
    #         res += (i + 1) // 2
        # return res
        
# @lc code=end

