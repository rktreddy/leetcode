#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     """ Approach 1: Check All Substrings O(n^3), O(1) """
    #     def check(i, j):
    #         left = i
    #         right = j - 1

    #         while left < right:
    #             if s[left] != s[right]:
    #                 return False
                
    #             left += 1
    #             right -= 1

    #         return True
        
    #     for length in range(len(s), 0, -1):
    #         for start in range(len(s) - length + 1):
    #             if check(start, start + length):
    #                 return s[start: start + length]
    #     return ""
        
    # def longestPalindrome(self, s: str) -> str:
    #     """ Approach 2: Dynamic Programming O(n^2), O(n^2) """
    #     n = len(s)
    #     dp = [[False] * n for _ in range(n)]
    #     ans = [0, 0]

    #     for i in range(n):
    #         dp[i][i] = True

    #     for i in range(n - 1):
    #         if s[i] == s[i + 1]:
    #             dp[i][i + 1] = True
    #             ans = [i, i + 1]
        
    #     for diff in range(2, n):
    #         for i in range(n - diff): 
    #             j = i + diff
    #             if s[i] == s[j] and dp[i + 1][j - 1]:
    #                 dp[i][j] = True
    #                 ans = [i, j]

    #     i, j = ans
    #     return s[i : j + 1]
    

    # def longestPalindrome(self, s: str) -> str:
    #     """ Approach 3: Expand From Centers O(n^2), o(n) """
    #     def expand(i, j):
    #         left = i
    #         right = j

    #         while left >= 0 and right < len(s) and s[left] == s[right]:
    #             left -= 1
    #             right += 1

    #         return right - left - 1
               
    #     ans = [0, 0]

    #     for i in range(len(s)):
    #         odd_length = expand(i, i)
    #         if odd_length > ans[1] - ans[0] + 1:
    #             dist = odd_length // 2
    #             ans = [i - dist, i + dist]

    #         even_length = expand(i, i + 1)
    #         if even_length > ans[1] - ans[0] + 1:
    #             dist = even_length // 2 - 1
    #             ans = [i - dist, i + 1 + dist]

    #     i, j = ans
    #     return s[i : j + 1]
    
    # def longestPalindrome(self, s: str) -> str:
    #     """ Neetcode: Expand From Centers O(n^2), o(1) """
    #     resIdx = 0
    #     resLen = 0

    #     for i in range(len(s)):
    #         # odd length
    #         l, r = i, i
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if (r - l + 1) > resLen:
    #                 resIdx = l
    #                 resLen = r - l + 1
    #             l -= 1
    #             r += 1

    #         # even length
    #         l, r = i, i + 1
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if (r - l + 1) > resLen:
    #                 resIdx = l
    #                 resLen = r - l + 1
    #             l -= 1
    #             r += 1

    #     return s[resIdx : resIdx + resLen]
    
    def longestPalindrome(self, s: str) -> str:
        """ practice: Neetcode: Expand From Centers O(n^2), o(1) """
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r -l + 1 > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length palindrome
            l, r = i, i + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r -l + 1 > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]
            
            

    # def longestPalindrome(self, s: str) -> str:
    #     """ Approach 4: Manacher's Algorithm  O(n), O(n) """
    #     s_prime = "#" + "#".join(s) + "#"
    #     n = len(s_prime)
    #     palindrome_radii = [0] * n
    #     center = radius = 0

    #     for i in range(n):
    #         mirror = 2 * center - i

    #         if i < radius:
    #             palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

    #         while (
    #             i + 1 + palindrome_radii[i] < n
    #             and i - 1 - palindrome_radii[i] >= 0
    #             and s_prime[i + 1 + palindrome_radii[i]]
    #             == s_prime[i - 1 - palindrome_radii[i]]
    #         ):
    #             palindrome_radii[i] += 1

    #         if i + palindrome_radii[i] > radius:
    #             center = i
    #             radius = i + palindrome_radii[i]

    #     max_length = max(palindrome_radii)
    #     center_index = palindrome_radii.index(max_length)
    #     start_index = (center_index - max_length) // 2
    #     longest_palindrome = s[start_index : start_index + max_length]

    #     return longest_palindrome

# @lc code=end

