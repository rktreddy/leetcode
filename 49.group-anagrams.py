#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     """ Approach 1: Categorize by Sorted String O(NKlogK), O(NK) """
    #     ans = collections.defaultdict(list)
    #     for s in strs:
    #         ans[tuple(sorted(s))].append(s)
    #     return ans.values()
    
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     """ Approach 2: Categorize by Count O(NK), O(NK)"""
    #     ans = defaultdict(list)
    #     for s in strs:
    #         count = [0] * 26
    #         for c in s:
    #             count[ord(c) - ord("a")] += 1
    #         ans[tuple(count)].append(s)
    #     return list(ans.values())

    
# @lc code=end


# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         """ Neetcode O(m*n), O(m) """
#         ans = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             ans[tuple(count)].append(s)
#         return list(ans.values())

# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         """ practice: Approach 2: Categorize by Count O(NK), O(NK) """
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             res[tuple(count)].append(s)
#         return list(res.values())

