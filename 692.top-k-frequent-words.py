#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
from collections import Counter
from heapq import heappush, heappop


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p): # less than
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     """ Approach 1: Brute Force O(NlogN), O(N) """        
    #     cnt = Counter(words)
    #     return sorted(list(cnt.keys()), key=lambda x: (-cnt[x], x))[:k]
    
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     """ Approach 2: Max Heap O(N + k logN), O(N) """       
    #     cnt = Counter(words)
    #     heap = [(-freq, word) for word, freq in cnt.items()]
    #     heapify(heap)

    #     return [heappop(heap)[1] for _ in range(k)] 
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """ Approach 3: Min Heap O(N logk), O(N) """   
        cnt = Counter(words)
        h = []
        for word, freq in cnt.items():
            heappush(h, Pair(word, freq))
            if len(h) > k:
                heappop(h)
        return [p.word for p in sorted(h, reverse=True)]
    

    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     """ Approach 4: Bucket Sorting + Trie O(N), O(N) """
    #     n = len(words)
    #     cnt = Counter(words)
    #     bucket = [{} for _ in range(n+1)]
    #     self.k = k

    #     def add_word(trie: Mapping, word: str) -> None:
    #         root = trie
    #         for c in word:
    #             if c not in root:
    #                 root[c] = {}
    #             root = root[c]
    #         root['#'] = {}

    #     def get_words(trie: Mapping, prefix: str) -> List[str]:
    #         if self.k == 0:
    #             return []
    #         res = []
    #         if '#' in trie:
    #             self.k -= 1
    #             res.append(prefix)
    #         for i in range(26):
    #             c = chr(ord('a') + i)
    #             if c in trie:
    #                 res += get_words(trie[c], prefix+c)
    #         return res

    #     for word, freq in cnt.items():
    #         add_word(bucket[freq], word)

    #     res = []
    #     for i in range(n, 0, -1):
    #         if self.k == 0:
    #             return res
    #         if bucket[i]:
    #             res += get_words(bucket[i], '')
    #     return res

     def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """ cracking faang: custom heap O(N), O(N) """

        
# @lc code=end

# # chatgpt solution
# ptimal Python Solution (Heap + HashMap) O(n log k) O(N)
# import heapq
# from collections import Counter

# class Solution:
#     def topKFrequent(self, words, k):
#         freq = Counter(words)

#         # Min-heap of size k
#         heap = []

#         for word, count in freq.items():
#             # Push using (-count, word) is WRONG in min-heap because it flips word order
#             # Instead use tuple: (count, reversed word sorting)
#             entry = (count, word)

#             if len(heap) < k:
#                 heapq.heappush(heap, entry)
#             else:
#                 # Compare with the smallest entry (min-heap root)
#                 if count > heap[0][0] or (count == heap[0][0] and word < heap[0][1]):
#                     heapq.heapreplace(heap, entry)

#         # Sort heap output: highest frequency first, lexicographical order next
#         heap.sort(key=lambda x: (-x[0], x[1]))

#         return [word for _, word in heap]


# # Clean Alternative (Pythonic & Accepted)
# class Solution:
#     def topKFrequent(self, words, k):
#         count = Counter(words)
#         return sorted(count.keys(), key=lambda w: (-count[w], w))[:k]


# # Want the absolute cleanest optimal version?
# class Solution:
#     def topKFrequent(self, words, k):
#         freq = Counter(words)
        
#         heap = []
#         for word, count in freq.items():
#             heapq.heappush(heap, (count, word))
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         result = sorted(heap, key=lambda x: (-x[0], x[1]))
#         return [w for _, w in result]
