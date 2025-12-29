#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
    #     # binary search over the length of substring
    #     # lo contains the valid value, and hi contains the
    #     # invalid value
    #     lo = 1
    #     hi = len(s) + 1
    #     while lo + 1 < hi:
    #         mid = lo + (hi - lo) // 2

    #         # can we make a valid substring of length `mid`?
    #         if self.__can_make_valid_substring(s, mid, k):
    #             # explore the right half
    #             lo = mid
    #         else:
    #             # explore the left half
    #             hi = mid

    #     # length of the longest substring that satisfies
    #     # the given condition
    #     return lo

    # def __can_make_valid_substring(self, s: str, substring_length: int, k: int):
    #     # take a window of length `substring_length` on the given
    #     # string, and move it from left to right. If this window
    #     # satisfies the condition of a valid string, then we return
    #     # true
    #     freq_map = {}
    #     max_frequency = 0
    #     start = 0
    #     for end in range(len(s)):
    #         freq_map[s[end]] = freq_map.get(s[end], 0) + 1

    #         # if the window [start, end] exceeds substring_length
    #         # then move the start pointer one step toward right
    #         if end + 1 - start > substring_length:
    #             # before moving the pointer toward right, decrease
    #             # the frequency of the corresponding character
    #             freq_map[s[start]] -= 1
    #             start += 1

    #         # record the maximum frequency seen so far
    #         max_frequency = max(max_frequency, freq_map[s[end]])
    #         if substring_length - max_frequency <= k:
    #             return True

    #     # we didn't a valid substring of the given size
    #     return False
    
    # def characterReplacement(self, s: str, k: int) -> int:
    #     """ Approach 2: Sliding Window (Slow) O(mn), O(m) """
    #     all_letters = set(s)
    #     max_length = 0

    #     # iterate over each unique letter
    #     for letter in all_letters:
    #         start = 0
    #         count = 0

    #         # initialize a sliding window for each unique letter
    #         for end in range(len(s)):
    #             if s[end] == letter:
    #                 # if the letter matches, increase the count
    #                 count += 1

    #             # bring start forward until the window is valid again
    #             while not self.__is_window_valid(start, end, count, k):
    #                 if s[start] == letter:
    #                     # if the letter matches, decrease the count
    #                     count -= 1
    #                 start += 1

    #             # at this point the window is valid, update max_length
    #             max_length = max(max_length, end + 1 - start)

    #     return max_length

    # def __is_window_valid(self, start: int, end: int, count: int, k: int):
    #     return end + 1 - start - count <= k
    
    # def characterReplacement(self, s: str, k: int) -> int:
    #     """ Approach 3: Sliding Window (Fast) O(n), O(m) """
    #     start = 0
    #     frequency_map = {}
    #     max_frequency = 0
    #     longest_substring_length = 0
    #     for end in range(len(s)):
    #         frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1

    #         # the maximum frequency we have seen in any window yet
    #         max_frequency = max(max_frequency, frequency_map[s[end]])

    #         # move the start pointer towards right if the current
    #         # window is invalid
    #         is_valid = (end + 1 - start - max_frequency <= k)
    #         if not is_valid:
    #             frequency_map[s[start]] -= 1
    #             start += 1

    #         # the window is valid at this point, store length
    #         # size of the window never decreases
    #         longest_substring_length = end + 1 - start

    #     return longest_substring_length


    # def characterReplacement(self, s: str, k: int) -> int:
    #     """ Neetcode 3: Sliding Window (Optimal) O(26 * n), O(m) """
    #     res = 0
    #     charSet = set(s)

    #     for c in charSet:
    #         count = l = 0
    #         for r in range(len(s)):
    #             if s[r] == c:
    #                 count += 1

    #             while (r - l + 1) - count > k:
    #                 if s[l] == c:
    #                     count -= 1
    #                 l += 1

    #             res = max(res, r - l + 1)
    #     return res
    

    # def characterReplacement(self, s: str, k: int) -> int:
    #     """ Neetcode 3: Sliding Window (Optimal) O(n), O(m) """
    #     count = {}
    #     res = 0

    #     l = 0
    #     maxf = 0
    #     for r in range(len(s)):
    #         count[s[r]] = 1 + count.get(s[r], 0)
    #         maxf = max(maxf, count[s[r]])

    #         while (r - l + 1) - maxf > k:
    #             count[s[l]] -= 1
    #             l += 1
    #         res = max(res, r - l + 1)

        # return res
    
    def characterReplacement(self, s: str, k: int) -> int:
        """ practice; Neetcode 3: Sliding Window (Optimal) O(n), O(m) """
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

        
# @lc code=end

