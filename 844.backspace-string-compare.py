#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
import itertools
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """ Approach #1: Build String [Accepted] O(m + n), O(1) """
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)
        
    # def backspaceCompare(self, S, T):
    #     """ Approach #2: Two Pointer [Accepted] O(m + n), O(1) """
    #     def F(S):
    #         skip = 0
    #         for x in reversed(S):
    #             if x == '#':
    #                 skip += 1
    #             elif skip:
    #                 skip -= 1
    #             else:
    #                 yield x

    #     return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
    
# @lc code=end

