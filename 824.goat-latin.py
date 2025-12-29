#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    # def toGoatLatin(self, sentence: str) -> str:
    #     """ Approach 1: Just Strings O(n^2), O(n^2) """
    #     def proc(idx, word):
    #         if word[0] not in 'aeiouAEIOU':
    #             word = word[1:] + word[0]

    #         return word + 'ma' + ('a' * idx)

    #     return ' '.join([proc(i, w) for i, w in enumerate(sentence.split(), 1)])
    
    def toGoatLatin(self, sentence: str) -> str:
        """ practice: Approach 1: Just Strings O(n^2), O(n^2) """
        def proc(idx, word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[0]
            return word + 'ma' + ('a' * idx)
        return ' '.join([proc(i, w) for i, w in enumerate(sentence.split(), 1)])
        
# @lc code=end

