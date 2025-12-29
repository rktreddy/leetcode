#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    # def isAlienSorted(self, words: List[str], order: str) -> bool:
    #     order_map = {}
    #     for index, val in enumerate(order):
    #         order_map[val] = index

    #     for i in range(len(words) - 1):

    #         for j in range(len(words[i])):
    #             # If we do not find a mismatch letter between words[i] and words[i + 1],
    #             # we need to examine the case when words are like ("apple", "app").
    #             if j >= len(words[i + 1]): return False

    #             if words[i][j] != words[i + 1][j]:
    #                 if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
    #                 # if we find the first different character and they are sorted,
    #                 # then there's no need to check remaining letters
    #                 break

    #     return True
    
    # def isAlienSorted(self, words: List[str], order: str) -> bool:
    #     """ cracking faang (M), N=26, S:O(1), M is sum of all lengths of words  """
    #     self.order_dict = {letter: i for i, letter in enumerate(order)}
    #     for word1, word2 in zip(words, words[1:]):
    #         if not self.words_are_lexico(word1, word2):
    #             return False
    #     return True
    # def words_are_lexico(self, word1, word2):
    #     for i in range(min(len(word1), len(word2))):
    #         if self.order_dict[word1[i]] != self.order_dict[word2[i]]:
    #             if self.order_dict[word1[i]] < self.order_dict[word2[i]]:
    #                 return True
    #             else:
    #                 return False
    #     return len(word1) <= len(word2)
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """ practice: cracking faang (M), N=26, S:O(1), M is sum of all lengths of words  """
        self.order_dict = {letter: i for i, letter in enumerate(order)}
        for word1, word2 in zip(words, words[1:]):
            if not self.words_not_lexico(word1, word2):
                return False
        return True
    
    def words_not_lexico(self, word1, word2):
        for i in range(min(len(word1), len(word2))):
            if self.order_dict[word1[i]] != self.order_dict[word2[i]]:
                if self.order_dict[word1[i]] < self.order_dict[word2[i]]:
                    return True
                else:
                    return False
        return len(word1) <= len(word2)
        
# @lc code=end
""" Approach 1: Compare adjacent words T:O(M+N)=> O(M), N=26, S:O(1) """
        
