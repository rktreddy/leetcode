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
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check_palindrome(s, i + 1, j) or check_palindrome(s, i, j - 1)
            i += 1
            j -= 1
        return True


# @lc code=end

