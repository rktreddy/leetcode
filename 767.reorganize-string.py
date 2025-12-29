#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    # def reorganizeString(self, s: str) -> str:
    #     """ Approach 1: Counting and Priority Queue O(N log k), O(k) """
    #     ans = []
    #     # Min heap ordered by character counts, so we will use
    #     # negative values for count
    #     pq = [(-count, char) for char, count in Counter(s).items()]
    #     heapify(pq)

    #     while pq:
    #         count_first, char_first = heappop(pq)
    #         if not ans or char_first != ans[-1]:
    #             ans.append(char_first)
    #             if count_first + 1 != 0: 
    #                 heappush(pq, (count_first + 1, char_first))
    #         else:
    #             if not pq: return ''
    #             count_second, char_second = heappop(pq)
    #             ans.append(char_second)
    #             if count_second + 1 != 0:
    #                 heappush(pq, (count_second + 1, char_second))
    #             heappush(pq, (count_first, char_first))

    #     return ''.join(ans)
    
    
    def reorganizeString(self, s: str) -> str:
        """ Approach 2: Counting and Odd/Even O(N), O(k) """
        char_counts = Counter(s)
        max_count, letter = 0, ''
        for char, count in char_counts.items():
            if count > max_count:
                max_count = count
                letter = char
        if max_count > (len(s) + 1) // 2:
            return ""
        ans = [''] * len(s)
        index = 0

        # Place the most frequent letter
        while char_counts[letter] != 0:
            ans[index] = letter
            index += 2
            char_counts[letter] -= 1

        # Place rest of the letters in any order
        for char, count in char_counts.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1

        return ''.join(ans)

        
# @lc code=end

