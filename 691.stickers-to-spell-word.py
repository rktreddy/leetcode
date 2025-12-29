#
# @lc app=leetcode id=691 lang=python3
#
# [691] Stickers to Spell Word
#

# @lc code=start
class Solution:
    # def minStickers(self, stickers: List[str], target: str) -> int:
    #     """ Approach 1: Optimized Exhaustive Search """
    #     t_count = collections.Counter(target)
    #     A = [collections.Counter(sticker) & t_count
    #          for sticker in stickers]

    #     for i in range(len(A) - 1, -1, -1):
    #         if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
    #             A.pop(i)

    #     self.best = len(target) + 1
    #     def search(ans = 0):
    #         if ans >= self.best: return
    #         if not A:
    #             if all(t_count[letter] <= 0 for letter in t_count):
    #                 self.best = ans
    #             return

    #         sticker = A.pop()
    #         used = max((t_count[letter] - 1) // sticker[letter] + 1
    #                     for letter in sticker)
    #         used = max(used, 0)

    #         for c in sticker:
    #             t_count[c] -= used * sticker[c]

    #         search(ans + used)
    #         for i in range(used - 1, -1, -1):
    #             for letter in sticker:
    #                 t_count[letter] += sticker[letter]
    #             search(ans + i)

    #         A.append(sticker)

    #     search()
    #     return self.best if self.best <= len(target) else -1

    # def minStickers(self, stickers: List[str], target: str) -> int:
    #     """ Top voted on LC """
    #     n = len(target)
    #     maxMask = 1 << n
    #     # dp[i] := min # of stickers to spell out i, where i is the bit mask of
    #     # target.
    #     dp = [float('inf')] * maxMask
    #     dp[0] = 0
        
    #     # Preprocess the stickers to create a mapping of character frequencies
    #     stickerCounts = []
    #     for sticker in stickers:
    #         stickerCounts.append(collections.Counter(sticker))
        
    #     for mask in range(maxMask):
    #         if dp[mask] == float('inf'):
    #             continue
    #         # Try to expand from `mask` by using each sticker.
    #         for i, stickerCount in enumerate(stickerCounts):
    #             # Skip over stickers that do not contain any characters we need
    #             if not any(c in stickerCount for c in target):
    #                 continue
    #             superMask = mask
    #             for c, freq in stickerCount.items():
    #                 for j, t in enumerate(target):
    #                     # Try to apply it on a missing char.
    #                     if c == t and not (superMask >> j & 1):
    #                         superMask |= 1 << j
    #                         freq -= 1
    #                         if freq == 0:
    #                             break
    #             dp[superMask] = min(dp[superMask], dp[mask] + 1)
        
    #     return -1 if dp[-1] == float('inf') else dp[-1]
        

    # def minStickers(self, stickers: List[str], target: str) -> int:
    #     """ cracking faang: O(2^N * M), O(N) """
    #     sticker_counts = [collections.Counter(sticker) for sticker in stickers]
    #     memo = {}
    #     def dfs(target_str):
    #         if not target_str:
    #             return 0
    #         if target_str in memo:
    #             return memo[target_str]
    #         target_counter = collections.Counter(target_str)
    #         ans = float('inf')
    #         for sticker in sticker_counts:
    #             if target_str[0] not in sticker:
    #                 continue
    #             remaining_characters = target_counter - sticker
    #             letters = [char * count for char, count in remaining_characters.items()]
    #             next_target = "".join(letters)
    #             ans = min(ans, 1 + dfs(next_target))
    #         memo[target_str] = ans
    #         return ans
    #     ans = dfs(target)
    #     return ans if ans != float('inf') else -1
    
    def minStickers(self, stickers: List[str], target: str) -> int:
        """ practice: cracking faang: O(2^N * M), O(N) """
        sticker_counts = [collections.Counter(sticker) for sticker in stickers]
        memo = {}
        def dfs(target_str):
            if not target_str:
                return 0
            if target_str in memo:
                return memo[target_str]
            ans = float('inf')
            for sticker_count in sticker_counts:
                target_counts = collections.Counter(target_str)
                if target_str[0] not in sticker_count:
                    continue
                remaining_chars = target_counts - sticker_count
                next_target = "".join([c * count for c, count in remaining_chars.items()])
                ans = min(ans, 1 + dfs(next_target))
            memo[target_str] = ans
            return ans

        ans = dfs(target)
        return ans if ans != float('inf') else -1


    
    # def minStickers(self, stickers: List[str], target: str) -> int:
    #     """ practice with lru_cache: cracking faang: O(2^N * M), O(N) """
    #     sticker_counts = [collections.Counter(sticker) for sticker in stickers]
    #     # memo = {}
    #     @lru_cache(None)
    #     def dfs(target_str):
    #         if not target_str:
    #             return 0
    #         # if target_str in memo:
    #         #     return memo[target_str]
    #         target_counter = collections.Counter(target_str)
    #         ans = float('inf')
    #         for sticker_count in sticker_counts:
    #             if target_str[0] not in sticker_count:
    #                 continue
    #             rem_chars = target_counter - sticker_count
    #             next_target = "".join([c * count for c, count in rem_chars.items()])
    #             ans = min(ans, 1 + dfs(next_target))
    #         # memo[target_str] = ans
    #         return ans
    #     ans = dfs(target)
    #     return ans if ans != float('inf') else -1
    
    # def minStickers(self, stickers: List[str], target: str) -> int:
    #     """ chatgpt soln using lru_cache """
    #     sticker_counts = [collections.Counter(s) for s in stickers]

    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dfs(remain):
    #         if not remain:
    #             return 0

    #         target_count = collections.Counter(remain)
    #         ans = float('inf')

    #         for sticker in sticker_counts:
    #             if remain[0] not in sticker:
    #                 continue

    #             new_count = target_count - sticker
    #             next_remain = "".join(sorted(c * n for c, n in new_count.items()))
    #             ans = min(ans, 1 + dfs(next_remain))

    #         return ans

    #     res = dfs(target)
    #     return res if res != float('inf') else -1


# @lc code=end

## counter subtract example
# from collections import Counter

# c1 = Counter(a=4, b=3, c=10)
# c2 = Counter(a=10, b=3, c=4)

# c3 = c1 - c2
# print(c3)
# # Output: Counter({'C': 6})