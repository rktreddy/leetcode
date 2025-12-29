#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
# class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     """ Approach 1: Breadth First Search: O(M^2 N), O(M^2 N) """
    #     from collections import defaultdict

    #     if (
    #         endWord not in wordList
    #         or not endWord
    #         or not beginWord
    #         or not wordList
    #     ):
    #         return 0

    #     # Since all words are of same length.
    #     L = len(beginWord)

    #     # Dictionary to hold combination of words that can be formed,
    #     # from any given word. By changing one letter at a time.
    #     all_combo_dict = defaultdict(list)
    #     for word in wordList:
    #         for i in range(L):
    #             # Key is the generic word
    #             # Value is a list of words which have the same intermediate generic word.
    #             all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

    #     # Queue for BFS
    #     queue = collections.deque([(beginWord, 1)])
    #     # Visited to make sure we don't repeat processing same word.
    #     visited = {beginWord: True}
    #     while queue:
    #         current_word, level = queue.popleft()
    #         for i in range(L):
    #             # Intermediate words for current word
    #             intermediate_word = (
    #                 current_word[:i] + "*" + current_word[i + 1 :]
    #             )

    #             # Next states are all the words which share the same intermediate state.
    #             for word in all_combo_dict[intermediate_word]:
    #                 # If at any point if we find what we are looking for
    #                 # i.e. the end word - we can return with the answer.
    #                 if word == endWord:
    #                     return level + 1
    #                 # Otherwise, add it to the BFS Queue. Also mark it visited
    #                 if word not in visited:
    #                     visited[word] = True
    #                     queue.append((word, level + 1))
    #             all_combo_dict[intermediate_word] = []
    #     return 0
    
        
# from collections import defaultdict
# class Solution(object):
#     """ Approach 2: Bidirectional Breadth First Search: O(M^2 N), O(M^2 N) """
#     def __init__(self):
#         self.length: int = 0
#         # Dictionary to hold combination of words that can be formed,
#         # from any given word. By changing one letter at a time.
#         self.all_combo_dict: Dict[str, List[str]] = defaultdict(list)

#     def visitWordNode(
#         self,
#         queue: Deque[str],
#         visited: Dict[str, int],
#         others_visited: Dict[str, int],
#     ) -> Any:
#         queue_size: int = len(queue)
#         for _ in range(queue_size):
#             current_word: str = queue.popleft()
#             for i in range(self.length):
#                 # Intermediate words for current word
#                 intermediate_word: str = (
#                     current_word[:i] + "*" + current_word[i + 1 :]
#                 )

#                 # Next states are all the words which share the same intermediate state.
#                 for word in self.all_combo_dict[intermediate_word]:
#                     # If the intermediate state/word has already been visited from the
#                     # other parallel traversal this means we have found the answer.
#                     if word in others_visited:
#                         return visited[current_word] + others_visited[word]
#                     if word not in visited:
#                         # Save the level as the value of the dictionary, to save number of hops.
#                         visited[word] = visited[current_word] + 1
#                         queue.append(word)

#         return None

#     def ladderLength(
#         self, beginWord: str, endWord: str, wordList: List[str]
#     ) -> int:
#         if (
#             endWord not in wordList
#             or not endWord
#             or not beginWord
#             or not wordList
#         ):
#             return 0

#         # Since all words are of same length.
#         self.length = len(beginWord)

#         for word in wordList:
#             for i in range(self.length):
#                 # Key is the generic word
#                 # Value is a list of words which have the same intermediate generic word.
#                 self.all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

#         # Queues for birdirectional BFS
#         queue_begin: Deque[str] = collections.deque(
#             [beginWord]
#         )  # BFS starting from beginWord
#         queue_end: Deque[str] = collections.deque(
#             [endWord]
#         )  # BFS starting from endWord

#         # Visited to make sure we don't repeat processing same word
#         visited_begin: Dict[str, int] = {beginWord: 1}
#         visited_end: Dict[str, int] = {endWord: 1}
#         ans: Any = None

#         # We do a birdirectional search starting one pointer from begin
#         # word and one pointer from end word. Hopping one by one.
#         while queue_begin and queue_end:

#             # Progress forward one step from the shorter queue
#             if len(queue_begin) <= len(queue_end):
#                 ans = self.visitWordNode(
#                     queue_begin, visited_begin, visited_end
#                 )
#             else:
#                 ans = self.visitWordNode(queue_end, visited_end, visited_begin)
#             if ans:
#                 return ans

#         return 0

class Solution(object):
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     """ cracking Faang: Breadth First Search: O(M^2 N), O(M^2 N) """
    #     # Edge case
    #     if beginWord == endWord or not wordList or endWord not in wordList:
    #         return 0
        
    #     # Build graph
    #     graph = collections.defaultdict(list)
    #     for word in wordList: # O(N) 
    #         for i in range(len(word)): # O(M)
    #             transform = word[:i] + '*' + word[i + 1:] # O(M)
    #             graph[transform].append(word)

    #     # BFS
    #     queue = collections.deque([(beginWord, 1)])
    #     visited = set([beginWord])
    #     while queue:
    #         word, distance = queue.popleft()
    #         if word == endWord:
    #             return distance
    #         visited.add(word)
    #         for i in range(len(word)):
    #             transformed = word[:i] + '*' + word[i + 1:]
    #             potential_words = graph[transformed]
    #             for potential_word in potential_words:
    #                 if potential_word not in visited:
    #                     queue.append((potential_word, distance + 1))
        
    #     return 0
    
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     """ chatgpt: Breadth First Search: O(M^2 N), O(M^2 N) """
    #     if endWord not in wordList:
    #         return 0
        
    #     L = len(beginWord)

    #     # Build pattern graph:  e.g., h*t → [hot, hit]
    #     graph = collections.defaultdict(list)
    #     for word in wordList:
    #         for i in range(L):
    #             pattern = word[:i] + "*" + word[i+1:]
    #             graph[pattern].append(word)
        
    #     # BFS
    #     queue = collections.deque([(beginWord, 1)])
    #     visited = {beginWord}

    #     while queue:
    #         word, dist = queue.popleft()

    #         if word == endWord:
    #             return dist

    #         # Expand neighbors
    #         for i in range(L):
    #             pattern = word[:i] + "*" + word[i+1:]
    #             neighbors = graph[pattern]

    #             for nxt in neighbors:
    #                 if nxt not in visited:
    #                     visited.add(nxt)
    #                     queue.append((nxt, dist + 1))
                
    #             # Optional optimization: remove pattern after use
    #             graph[pattern] = []

    #     return 0
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ chatgpt: Breadth First Search: O(M^2 N), O(M^2 N) """
        # Edge case
        if beginWord == endWord or not wordList or endWord not in wordList:
            return 0
        # Build graph
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)

        queue = collections.deque([(beginWord, 1)])
        visted = set([beginWord])

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for nei in graph[pattern]:
                    if nei not in visted:
                        visted.add(nei)
                        queue.append((nei, dist + 1))
            # Optional optimization: remove pattern after use
            graph[pattern] = []

        return 0
            
                
# @lc code=end

