#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter

class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     """ Approach 1: Sliding Window O(|S| + |T|), O(|S| + |T|)  """
    #     if not t or not s:
    #         return ""

    #     # Dictionary which keeps a count of all the unique characters in t.
    #     dict_t = Counter(t)

    #     # Number of unique characters in t, which need to be present in the desired window.
    #     required = len(dict_t)

    #     # left and right pointer
    #     l, r = 0, 0

    #     # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    #     # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    #     formed = 0

    #     # Dictionary which keeps a count of all the unique characters in the current window.
    #     window_counts = {}

    #     # ans tuple of the form (window length, left, right)
    #     ans = float("inf"), None, None

    #     while r < len(s):

    #         # Add one character from the right to the window
    #         character = s[r]
    #         window_counts[character] = window_counts.get(character, 0) + 1

    #         # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
    #         if (
    #             character in dict_t
    #             and window_counts[character] == dict_t[character]
    #         ):
    #             formed += 1

    #         # Try and contract the window till the point where it ceases to be 'desirable'.
    #         while l <= r and formed == required:
    #             character = s[l]

    #             # Save the smallest window until now.
    #             if r - l + 1 < ans[0]:
    #                 ans = (r - l + 1, l, r)

    #             # The character at the position pointed by the `left` pointer is no longer a part of the window.
    #             window_counts[character] -= 1
    #             if (
    #                 character in dict_t
    #                 and window_counts[character] < dict_t[character]
    #             ):
    #                 formed -= 1

    #             # Move the left pointer ahead, this would help to look for a new window.
    #             l += 1

    #         # Keep expanding the window once we are done contracting.
    #         r += 1
    #     return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

        
    # def minWindow(self, s: str, t: str) -> str:
    #     """ Approach 2: Optimized Sliding Window O(|S| + |T|), O(|S| + |T|) """
    #     if not t or not s:
    #         return ""

    #     dict_t = Counter(t)

    #     required = len(dict_t)

    #     # Filter all the characters from s into a new list along with their index.
    #     # The filtering criteria is that the character should be present in t.
    #     filtered_s = []
    #     for i, char in enumerate(s):
    #         if char in dict_t:
    #             filtered_s.append((i, char))

    #     l, r = 0, 0
    #     formed = 0
    #     window_counts = {}

    #     ans = float("inf"), None, None

    #     # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    #     # Hence, we follow the sliding window approach on as small list.
    #     while r < len(filtered_s):
    #         character = filtered_s[r][1]
    #         window_counts[character] = window_counts.get(character, 0) + 1

    #         if window_counts[character] == dict_t[character]:
    #             formed += 1

    #         # If the current window has all the characters in desired frequencies i.e. t is present in the window
    #         while l <= r and formed == required:
    #             character = filtered_s[l][1]

    #             # Save the smallest window until now.
    #             end = filtered_s[r][0]
    #             start = filtered_s[l][0]
    #             if end - start + 1 < ans[0]:
    #                 ans = (end - start + 1, start, end)

    #             window_counts[character] -= 1
    #             if window_counts[character] < dict_t[character]:
    #                 formed -= 1
    #             l += 1

    #         r += 1
    #     return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
    
    # def minWindow(self, s: str, t: str) -> str:
    #     """ Top voted solution """
    #     need, missing = collections.Counter(t), len(t)
    #     i = I = J = 0
    #     for j, c in enumerate(s, 1):
    #         missing -= need[c] > 0
    #         need[c] -= 1
    #         if not missing:
    #             while i < j and need[s[i]] < 0:
    #                 need[s[i]] += 1
    #                 i += 1
    #             if not J or j - i <= J - I:
    #                 I, J = i, j 
    #     return s[I:J]


    # def minWindow(self, s: str, t: str) -> str:
    #     """ ChatGPT sliding window O(|s| + |t|), O(|s| + |t|) """
    #     if not s or not t:
    #         return ""

    #     # Count characters in t
    #     target_count = Counter(t)
    #     required = len(target_count)  # Number of unique characters in t
    #     window_count = {}
        
    #     # Pointers for the sliding window
    #     left, right = 0, 0
    #     formed = 0  # Number of unique characters in the current window matching the target
    #     min_length = float("inf")
    #     min_window = (0, 0)  # To store the start and end index of the minimum window
        
    #     # Expand the window with right pointer
    #     while right < len(s):
    #         char = s[right]
    #         window_count[char] = window_count.get(char, 0) + 1

    #         # Check if the current character frequency matches the target
    #         if char in target_count and window_count[char] == target_count[char]:
    #             formed += 1

    #         # Contract the window with left pointer while the window is valid
    #         while left <= right and formed == required:
    #             char = s[left]
                
    #             # Update the minimum window if it's smaller than the previous ones
    #             if right - left + 1 < min_length:
    #                 min_length = right - left + 1
    #                 min_window = (left, right)

    #             # Remove the left character from the window count
    #             window_count[char] -= 1
    #             if char in target_count and window_count[char] < target_count[char]:
    #                 formed -= 1

    #             # Move the left pointer forward to find a smaller valid window
    #             left += 1

    #         # Move the right pointer forward to expand the window
    #         right += 1

    #     # Extract the minimum window substring
    #     start, end = min_window
    #     return s[start:end + 1] if min_length != float("inf") else ""

    # def minWindow(self, s: str, t: str) -> str:
    #     """ practice: ChatGPT sliding window O(|s| + |t|), O(|s| + |t|) """
    #     if not s or not t:
    #         return ""
        
    #     target_count = Counter(t)
    #     required = len(target_count)

    #     window_count = {}
    #     formed = 0

    #     left, right = 0, 0
        
    #     min_length = float("inf")
    #     min_window = (0, 0)

    #     while right < len(s):
    #         char = s[right]
    #         window_count[char] = window_count.get(char, 0) + 1
    #         if char in target_count and window_count[char] == target_count[char]:
    #             formed += 1
            
    #         while left <= right and formed == required:
    #             char = s[left]

    #             if right - left + 1 < min_length:
    #                 min_length = right - left + 1
    #                 min_window = (left, right)

    #             window_count[char] -= 1
    #             if char in target_count and window_count[char] < target_count[char]:
    #                 formed -= 1

    #             left += 1

    #         right += 1
        
    #     start, end = min_window

    #     return s[start : end + 1] if min_length != float("inf") else ""
    
    # def minWindow(self, s: str, t: str) -> str:
    #     """ practice: ChatGPT sliding window O(|s| + |t|), O(|s| + |t|) """
    #     if not s or not t:
    #         return ""
        
    #     target_count = Counter(t)
    #     target_uniqlen = len(target_count)

    #     window_count = {}
    #     window_uniqlen = 0

    #     left, right = 0, 0

    #     min_length = float("inf")
    #     min_window = (0, 0)
        
    #     while right < len(s):
    #         char = s[right]
    #         window_count[char] = window_count.get(char, 0) + 1
    #         if char in target_count and window_count[char] == target_count[char]:
    #             window_uniqlen += 1

    #         while left <= right and window_uniqlen == target_uniqlen:
    #             char = s[left]

    #             if right - left + 1 < min_length:
    #                 min_length = right - left + 1
    #                 min_window = (left, right)

    #             window_count[char] -= 1
    #             if char in target_count and window_count[char] < target_count[char]:
    #                 window_uniqlen -= 1
            
    #             left += 1

    #         right += 1

    #     start, end = min_window

    #     return s[start : end + 1] if min_length != float("inf") else ""
    
    # def minWindow(self, s: str, t: str) -> str:
    #     """ practice: ChatGPT sliding window O(|s| + |t|), O(|s| + |t|) """
    #     if not s or not t:
    #         return ""
        
    #     target_count = Counter(t)
    #     target_uniqlen = len(target_count)
    #     window_count = {}
    #     window_uniqlen = 0

    #     left, right = 0, 0

    #     min_length = float("inf")
    #     min_window = (0, 0)

    #     while right < len(s):
    #         char = s[right]
    #         window_count[char] = window_count.get(char, 0) + 1

    #         if char in target_count and window_count[char] == target_count[char]:
    #             window_uniqlen += 1

    #         while left <= right and window_uniqlen == target_uniqlen:
    #             char = s[left]

    #             if right - left + 1 < min_length:
    #                 min_length = right - left + 1
    #                 min_window = (left, right)

    #             window_count[char] -= 1
    #             if char in target_count and window_count[char] < target_count[char]:
    #                 window_uniqlen -= 1

    #             left += 1

    #         right += 1

    #     start, end = min_window

    #     return s[start : end + 1] if min_length != float("inf") else ""

    # def minWindow(self, s: str, t: str) -> str:
    #     """ Neetcode: Sliding Window O(n + m), O(m) """
    #     if t == "":
    #         return ""

    #     countT, window = {}, {}
    #     for c in t:
    #         countT[c] = 1 + countT.get(c, 0)

    #     have, need = 0, len(countT)
    #     res, resLen = [-1, -1], float("infinity")
    #     l = 0
    #     for r in range(len(s)):
    #         c = s[r]
    #         window[c] = 1 + window.get(c, 0)

    #         if c in countT and window[c] == countT[c]:
    #             have += 1

    #         while have == need:
    #             if (r - l + 1) < resLen:
    #                 res = [l, r]
    #                 resLen = r - l + 1

    #             window[s[l]] -= 1
    #             if s[l] in countT and window[s[l]] < countT[s[l]]:
    #                 have -= 1
    #             l += 1
    #     l, r = res
    #     return s[l : r + 1] if resLen != float("infinity") else ""


    # def minWindow(self, s: str, t: str) -> str:
    #     """ practice: Neetcode: Sliding Window O(n + m), O(m) """
    #     if t == "":
    #         return ""
    #     countT, window = {}, {}
    #     for c in t:
    #         countT[c] = 1 + countT.get(c, 0)
    #     have, need = 0, len(countT)
    #     res, resLen = [-1, -1], float('inf')
    #     l = 0
    #     for r in range(len(s)):
    #         window[s[r]] = 1 + window.get(s[r], 0)
    #         if s[r] in countT and countT[s[r]] == window[s[r]]:
    #             have += 1

    #         while have == need:
    #             if (r - l + 1) < resLen:
    #                 res = [l, r]
    #                 resLen = r - l + 1

    #             window[s[l]] -= 1
    #             if s[l] in countT and window[s[l]] < countT[s[l]]:
    #                 have -= 1
    #             l += 1
    #     l, r = res
    #     return s[l : r + 1] if resLen != float('inf') else ""
    
    def minWindow(self, s: str, t: str) -> str:
        """ cracking faang: Sliding Window O(n + m), O(m) """
        if not s or not t or len(t) > len(s):
            return ""
        
        t_counts = collections.Counter(t)
        l = r = matches = 0
        required_matches = len(t_counts)
        window_counts = collections.defaultdict(int)
        ans = (float('inf'), 0, 0) # length, right, left

        while r < len(s):
            cur_char = s[r]
            window_counts[cur_char] += 1
            if cur_char in t_counts and t_counts[cur_char] == window_counts[cur_char]:
                matches += 1

            while l <= r and matches == required_matches:
                to_remove = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[to_remove] -= 1

                if to_remove in t_counts and window_counts[to_remove] < t_counts[to_remove]:
                    matches -= 1
                
                l += 1

            r += 1

        return s[ans[1] : ans[2] + 1] if ans[0] != float('inf') else ""


# @lc code=end

