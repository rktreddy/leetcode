#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    # def customSortString(self, order: str, s: str) -> str:
    #     """ in built sort o(n log n), o(n) """
    #     d = {c: i for i, c in enumerate(order)}
    #     return ''.join(sorted(s, key=lambda x: d.get(x, 0)))
    
    def customSortString(self, order: str, s: str) -> str:
        """ O(N), O(N) """
        cnt = Counter(s)
        ans = []
        for c in order:
            ans.append(c * cnt[c])
            cnt[c] = 0
        for c, v in cnt.items():
            ans.append(c * v)
        return ''.join(ans)
        
# @lc code=end

