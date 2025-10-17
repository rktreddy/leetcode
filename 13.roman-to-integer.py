#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
# values = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000,
# }

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         """ Approach 1: Left-to-Right Pass O(1), O(1) """
#         total = 0
#         i = 0
#         while i < len(s):
#             # If this is the subtractive case.
#             if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
#                 total += values[s[i + 1]] - values[s[i]]
#                 i += 2
#             # Else this is NOT the subtractive case.
#             else:
#                 total += values[s[i]]
#                 i += 1
#         return total

# values = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000,
#     "IV": 4,
#     "IX": 9,
#     "XL": 40,
#     "XC": 90,
#     "CD": 400,
#     "CM": 900,
# }


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         """ Approach 2: Left-to-Right Pass Improved O(1), O(1) """
#         total = 0
#         i = 0
#         while i < len(s):
#             # This is the subtractive case.
#             if i < len(s) - 1 and s[i : i + 2] in values:
#                 total += values[s[i : i + 2]]
#                 i += 2
#             else:
#                 total += values[s[i]]
#                 i += 1
#         return total
    

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    # def romanToInt(self, s: str) -> int:
    #     """ Approach 3: Right-to-Left Pass O(1), O(1) """
    #     total = values.get(s[-1])
    #     for i in reversed(range(len(s) - 1)):
    #         if values[s[i]] < values[s[i + 1]]:
    #             total -= values[s[i]]
    #         else:
    #             total += values[s[i]]
    #     return total

    def romanToInt(self, s: str) -> int:
        """ practice """
        total = values.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total


# @lc code=end

