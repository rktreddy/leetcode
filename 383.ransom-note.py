#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    # """ Approach1: simulation"""
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     for letter in ransomNote:
    #         if letter not in magazine:
    #             return False
    #         location = magazine.index(letter)
    #         magazine = magazine[:location] + magazine[location+1:]
    #     return True

    # """ Approach 2: popular code"""
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     st1, st2 = collections.Counter(ransomNote), collections.Counter(magazine)
    #     if st1 & st2 == st1:
    #         return True
    #     return False

    # """ Approach 3: Two hashtables"""
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     if len(ransomNote) > len(magazine):
    #         return False
        
    #     magazine_counts = collections.Counter(magazine)
    #     ransom_note_counts = collections.Counter(ransomNote)

    #     for char, count in ransom_note_counts.items():
    #         magazine_count = magazine_counts[char]
    #         if magazine_count < count:
    #             return False
    #     return True

    """ Approach 4"""
    def makeCountsMap(self, string):
        counts = {}
        for c in string:
            counts[c] = counts.get(c, 0) + 1
        return counts
    
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     if len(ransomNote) > len(magazine):
    #         return False
        
    #     # magazine_counts = collections.Counter(magazine)
    #     # ransom_note_counts = collections.Counter(ransomNote)
    #     magazine_counts = self.makeCountsMap(magazine)
    #     ransom_note_counts = self.makeCountsMap(ransomNote)

    #     for char, count in ransom_note_counts.items():
    #         magazine_count = magazine_counts.get(char, 0)
    #         if magazine_count < count:
    #             return False
    #     return True
    
    """ Approach 5: One hastable"""
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_counts = collections.Counter(magazine)
        # magazine_counts = self.makeCountsMap(magazine)
        for c in ransomNote:
            if magazine_counts.get(c, 0) <= 0:
                return False
            magazine_counts[c] -= 1
        return True
        
        
# @lc code=end

