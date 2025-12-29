#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    # def frequencySort(self, s: str) -> str:
    #     """ Approach 1: Arrays and Sorting O(n log n), O(n) """
        
    #     if not s: return s
        
    #     # Convert s to a list.
    #     s = list(s)
        
    #     # Sort the characters in s.
    #     s.sort()
        
    #     # Make a list of strings, one for each unique char.
    #     all_strings = []
    #     cur_sb = [s[0]]
    #     for c in s[1:]:
    #         # If the last character on string builder is different...
    #         if cur_sb[-1] != c:
    #             all_strings.append("".join(cur_sb))
    #             cur_sb = []
    #         cur_sb.append(c)
    #     all_strings.append("".join(cur_sb))
        
    #     # Sort the strings by length from *longest* to shortest.
    #     all_strings.sort(key=lambda string : len(string), reverse=True)
        
    #     # Convert to a single string to return.
    #     # Converting a list of strings to a string is often done
    #     # using this rather strange looking python idiom.
    #     return "".join(all_strings)
    
    # def frequencySort(self, s: str) -> str:
    #     """ Approach 2: HashMap and Sort O(n log n), O(n) """
    #     # Count up the occurances.
    #     counts = collections.Counter(s)

    #     # Build up the string builder.
    #     string_builder = []
    #     for letter, freq in counts.most_common():
    #         # letter * freq makes freq copies of letter.
    #         # e.g. "a" * 4 -> "aaaa"
    #         string_builder.append(letter * freq)
    #     return "".join(string_builder)
    
    def frequencySort(self, s: str) -> str:
        """ Approach 3: Multiset and Bucket Sort O(n), O(n) """
        if not s: return s

        # Determine the frequency of each character.
        counts = collections.Counter(s)
        max_freq = max(counts.values())

        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)
            
        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)
                
        return "".join(string_builder)
        
# @lc code=end

