#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# @lc code=start
class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """ Approach 1: Horizontal scanning O(S), O(1) """
    #     if len(strs) == 0:
    #         return ""
    #     prefix = strs[0]
    #     for i in range(1, len(strs)):
    #         while strs[i].find(prefix) != 0:
    #             prefix = prefix[0 : len(prefix) - 1]
    #             if prefix == "":
    #                 return ""
    #     return prefix
    
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """ Approach 2: Vertical scanning O(S), O(1) """
    #     if strs == None or len(strs) == 0:
    #         return ""
    #     for i in range(len(strs[0])):
    #         c = strs[0][i]
    #         for j in range(1, len(strs)):
    #             if i == len(strs[j]) or strs[j][i] != c:
    #                 return strs[0][0:i]
    #     return strs[0]
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ practice: Approach 2: Vertical scanning O(S), O(1) """
        if strs == None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or c != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
    
    #  def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """ Approach 3: Divide and conquer O(S), O(m log n) """
    #     if not strs:
    #         return ""

    #     def LCP(left, right):
    #         min_len = min(len(left), len(right))
    #         for i in range(min_len):
    #             if left[i] != right[i]:
    #                 return left[:i]
    #         return left[:min_len]

    #     def divide_and_conquer(strs, l, r):
    #         if l == r:
    #             return strs[l]
    #         else:
    #             mid = (l + r) // 2
    #             lcpLeft = divide_and_conquer(strs, l, mid)
    #             lcpRight = divide_and_conquer(strs, mid + 1, r)
    #             return LCP(lcpLeft, lcpRight)

    #     return divide_and_conquer(strs, 0, len(strs) - 1)
    
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """ Approach 4: Binary search O(S log m), O(1) """
    #     if not strs:
    #         return ""
    #     minLen = min(len(x) for x in strs)
    #     low, high = 1, minLen
    #     while low <= high:
    #         middle = (low + high) // 2
    #         if self.isCommonPrefix(strs, middle):
    #             low = middle + 1
    #         else:
    #             high = middle - 1
    #     return strs[0][: (low + high) // 2]

    # def isCommonPrefix(self, strs, l):
    #     str1 = strs[0][:l]
    #     for i in range(1, len(strs)):
    #         if not strs[i].startswith(str1):
    #             return False
    #     return True

    # def longestCommonPrefix(self, strings: List[str]) -> str:
    #     """ Algomonster: O(m * n), O(1) """
    #     # Assumes the input list of strings is not empty
    #     # The outer loop goes through each character of the first string
    #     for index in range(len(strings[0])):
    #         # Inner loop checks the character at the current position across all other strings
    #         for string in strings[1:]:
    #             # Checks if we've reached the end of any string or a character mismatch is found
    #             if index >= len(string) or string[index] != strings[0][index]:
    #                 # Return the longest common prefix found so far
    #                 return strings[0][:index]
    #     # If no early return happened, the first string itself is the common prefix
    #     return strings[0]

# @lc code=end

