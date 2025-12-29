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
    
    # def customSortString(self, order: str, s: str) -> str:
    #     cnt = Counter(s)
    #     ans = []
    #     for c in order:
    #         if c in cnt:
    #             ans.append(c * cnt[c])
    #             del cnt[c]
    #     for c, freq in cnt.items():
    #         ans.append(c * freq)
    #     return ''.join(ans)

    def customSortString(self, order: str, s: str) -> str:
        """ Approach 2: Frequency Table and Counting O(n), O(n) """
        count_s = Counter(s)
        res = []
        for c in order:
            if c in count_s:
                res.append(c * count_s[c])
                del count_s[c]
        for c, i in count_s.items():
            res.append(c * i)
        return ''.join(res)
        
# @lc code=end

# def customSortString(self, order: str, s: str) -> str:
    #     """ O(N), O(N) """
    #     cnt = Counter(s)
    #     ans = []
    #     for c in order:
    #         ans.append(c * cnt[c])
    #         cnt[c] = 0
    #     for c, v in cnt.items():
    #         ans.append(c * v)
    #     return ''.join(ans)
    
    # def customSortString(self, order: str, s: str) -> str:
    #     """ Approach 2: Frequency Table and Counting O(n), O(n) """
    #     s_elem_freq = Counter(s)
    #     s_permutation = []

    #     for char in order:
    #         # Elem to be Ordered
    #         if char in s_elem_freq:
    #             s_permutation.append(char * s_elem_freq[char])
    #             del s_elem_freq[char]

    #     for unordered_elem in s_elem_freq:
    #         s_permutation.append(unordered_elem * s_elem_freq[unordered_elem])

    #     return ''.join(s_permutation)