#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    # def maxVowels(self, s: str, k: int) -> int:
    #     """ Approach: Sliding Window O(n), O(1) """
    #     vowels = {'a', 'e', 'i', 'o', 'u'}
        
    #     # Build the window of size k, count the number of vowels it contains.
    #     count = 0
    #     for i in range(k):
    #         count += int(s[i] in vowels)
    #     answer = count
        
    #     # Slide the window to the right, focus on the added character and the
    #     # removed character and update "count". Record the largest "count".
    #     for i in range(k, len(s)):
    #         count += int(s[i] in vowels)
    #         count -= int(s[i - k] in vowels)
    #         answer = max(answer, count)
        
    #     return answer
    
    # def maxVowels(self, s: str, k: int) -> int:
    #     """ practice: Approach: Sliding Window O(n), O(1) """
    #     vowels = {'a', 'e', 'i', 'o', 'u'}
    #     count = 0
    #     for i in range(k):
    #         count += int(s[i] in vowels)
    #     answer = count
    #     for i in range(k, len(s)):
    #         count += int(s[i] in vowels) - int(s[i - k] in vowels)
    #         answer = max(answer, count)
    #     return answer

    def maxVowels(self, s: str, k: int) -> int:
        """ practice: Approach: Sliding Window O(n), O(1) """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count
        for i in range(k, len(s)):
            count += int(s[i] in vowels) - int(s[i - k] in vowels)
            answer = max(answer, count)
        return answer


# @lc code=end

