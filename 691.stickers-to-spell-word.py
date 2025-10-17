#
# @lc app=leetcode id=691 lang=python3
#
# [691] Stickers to Spell Word
#

# @lc code=start
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        """ Approach 1: Optimized Exhaustive Search """
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        self.best = len(target) + 1
        def search(ans = 0):
            if ans >= self.best: return
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count):
                    self.best = ans
                return

            sticker = A.pop()
            used = max((t_count[letter] - 1) // sticker[letter] + 1
                        for letter in sticker)
            used = max(used, 0)

            for c in sticker:
                t_count[c] -= used * sticker[c]

            search(ans + used)
            for i in range(used - 1, -1, -1):
                for letter in sticker:
                    t_count[letter] += sticker[letter]
                search(ans + i)

            A.append(sticker)

        search()
        return self.best if self.best <= len(target) else -1

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
        
# @lc code=end

