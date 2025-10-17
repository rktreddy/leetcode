#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
from collections import deque
class Solution:
    # def reverseWords(self, s: str) -> str:
    #     """ Approach 1: Built-in Split + Reverse, O(n), O(n) """
    #     return " ".join(reversed(s.split()))
        
    # def trim_spaces(self, s: str) -> list:
    #     """ Approach 2: Reverse the Whole String and Then Reverse Each Word O(n), O(n)"""
    #     left, right = 0, len(s) - 1
    #     # remove leading spaces
    #     while left <= right and s[left] == " ":
    #         left += 1

    #     # remove trailing spaces
    #     while left <= right and s[right] == " ":
    #         right -= 1

    #     # reduce multiple spaces to single one
    #     output = []
    #     while left <= right:
    #         if s[left] != " ":
    #             output.append(s[left])
    #         elif output[-1] != " ":
    #             output.append(s[left])
    #         left += 1

    #     return output

    # def reverse(self, l: list, left: int, right: int) -> None:
    #     while left < right:
    #         l[left], l[right] = l[right], l[left]
    #         left, right = left + 1, right - 1

    # def reverse_each_word(self, l: list) -> None:
    #     n = len(l)
    #     start = end = 0

    #     while start < n:
    #         # go to the end of the word
    #         while end < n and l[end] != " ":
    #             end += 1
    #         # reverse the word
    #         self.reverse(l, start, end - 1)
    #         # move to the next word
    #         start = end + 1
    #         end += 1

    # def reverseWords(self, s: str) -> str:
    #     # converst string to char array
    #     # and trim spaces at the same time
    #     l = self.trim_spaces(s)

    #     # reverse the whole string
    #     self.reverse(l, 0, len(l) - 1)

    #     # reverse each word
    #     self.reverse_each_word(l)

    #     return "".join(l)
        

    def reverseWords(self, s: str) -> str:
        """ Approach 3: Deque of Words O(n), O(n) """
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))

        return " ".join(d)
    
# @lc code=end

