#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    # def isPalindrome(self, s: str) -> bool:
        # # compare with reverse 
        # filtered_chars = filter(lambda ch: ch.isalnum(), s)
        # lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        # filtered_chars_list = list(lowercase_filtered_chars)
        # reversed_chars_list = filtered_chars_list[::-1]

        # return filtered_chars_list == reversed_chars_list

    # def isPalindrome(self, s: str) -> bool:
    #     """ Approach 2: Two Pointers O(n), O(1) """
    #     l, r = 0, len(s) - 1
    #     while l < r:
    #         while l < r and not s[l].isalnum():
    #             l += 1
    #         while l < r and not s[r].isalnum():
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l += 1
    #         r -= 1
    #     return True
    
    def isPalindrome(self, s: str) -> bool:
        """ practice: Approach 2: Two Pointers O(n), O(1) """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# @lc code=end

