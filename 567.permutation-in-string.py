#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ My first attempt O(n), O(1) """
        if len(s1) > len(s2):
            return False
        windowsize = len(s1)
        counts1 = {}
        counts2 = {}
        for i in range(windowsize):
            counts1[s1[i]] = counts1.get(s1[i], 0) + 1
            counts2[s2[i]] = counts2.get(s2[i], 0) + 1

        if counts1 == counts2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            counts2[s2[r]] = counts2.get(s2[r], 0) + 1
            counts2[s2[l]] = counts2.get(s2[r], 0) - 1

            if counts2[s2[l]] == 0:
                del counts2[s2[l]]
            l += 1
            if counts1 == counts2:
                return True

        return False
        
# @lc code=end


# def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s1) > len(s2):
    #         return False
        
    #     from collections import Counter
        
    #     count1 = Counter(s1)
    #     count2 = Counter(s2[:len(s1)])
        
    #     if count1 == count2:
    #         return True
        
    #     l = 0
    #     for r in range(len(s1), len(s2)):
    #         count2[s2[r]] += 1
    #         count2[s2[l]] -= 1
            
    #         if count2[s2[l]] == 0:
    #             del count2[s2[l]]
    #         l += 1
            
    #         if count1 == count2:
    #             return True
        
    #     return False


    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     """ My first attempt O(m * n), O(26) """
    #     counts1 = {}
    #     for c in s1:
    #         counts1[c] = counts1.get(c, 0) + 1
    #     windowsize = len(s1)
    #     for l in range(len(s2) + 1 - windowsize):
    #         counts2 = {}
    #         for r in range(l, l + windowsize):
    #             counts2[s2[r]] = 1 + counts2.get(s2[r], 0)
    #         if counts1 == counts2:
    #             return True

    #     return False

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     """ Chatgpt sliding window O(m * n), O(26) """
    #     if len(s1) > len(s2):
    #         return False
        
    #     count1 = Counter(s1)
    #     count2 = Counter(s2[:len(s1)])
    #     if count1 == count2:
    #         return True
        
    #     l = 0
    #     for r in range(len(s1), len(s2)):
    #         count2[s2[r]] += 1
    #         count2[s2[l]] -= 1

    #         if count2[s2[l]] == 0:
    #             del count2[s2[l]]
    #         l += 1

    #         if count1 == count2:
    #             return True

    #     return False