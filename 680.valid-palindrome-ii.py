#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    # def validPalindrome(self, s: str) -> bool:
    #     """ Approach: Two Pointers O(N), O(1) """
    #     def check_palindrome(s, i, j):
    #         while i < j:
    #             if s[i] != s[j]:
    #                 return False
                
    #             i += 1
    #             j -= 1
    #         return True
        
    #     i, j = 0, len(s) - 1
    #     while i < j:
    #         if s[i] != s[j]:
    #             return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
    #         i += 1
    #         j -= 1

    #     return True
    
    # def validPalindrome(self, s: str) -> bool:
    #     """ practice: Approach: Two Pointers O(N), O(1) """
    #     def check_palindrome(s, i, j):
    #         while i < j:
    #             if s[i] != s[j]:
    #                 return False
    #             i += 1
    #             j -= 1
    #         return True
        
    #     i, j = 0, len(s) - 1
    #     while i < j:
    #         if s[i] != s[j]:
    #             return check_palindrome(s, i + 1, j) or check_palindrome(s, i, j - 1)
    #         i += 1
    #         j -= 1
    #     return True

    def validPalindrome(self, s: str) -> bool:
        """ practice: Approach: Two Pointers O(N), O(1) """
        def check_palindrom(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check_palindrom(s, i + 1, j) or check_palindrom(s, i, j - 1)
            i += 1
            j -= 1
        return True


# @lc code=end

# Your updated function attempts to check if a string can become a palindrome
#  by recursively allowing more than one character to be removed. H

# def can_be_palindrome(S, max_removals=1):
#     """ best case O(n), worst case O(n*k) """
#     def helper(left, right, k):
#         while left < right:
#             if S[left] == S[right]:
#                 left += 1
#                 right -= 1
#             else:
#                 if k == 0:
#                     return False
#                 # Try skipping left OR skipping right
#                 return helper(left + 1, right, k - 1) or helper(left, right - 1, k - 1)
#         return True

#     return helper(0, len(S) - 1, max_removals)

# print(can_be_palindrome("abbca", 1))  # True  (remove c)
# print(can_be_palindrome("abcda", 2))  # True  (remove b and d)
# print(can_be_palindrome("abc", 1))    # False



