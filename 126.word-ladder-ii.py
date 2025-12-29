#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    """ Approach 1: Breadth-First Search (BFS) + Backtracking O(N K^2 + alpha), O(N K) """
    def __init__(self):
        self.adjList: Dict[str, List[str]] = {}
        self.currPath: List[str] = []
        self.shortestPaths: List[List[str]] = []

    def findNeighbors(self, word: str, wordSet: Set[str]) -> List[str]:
        neighbors: List[str] = []
        charList = list(word)
        for i in range(len(charList)):
            oldChar = charList[i]
            # replace the i-th character with all letters from a to z except the original character
            for c in "abcdefghijklmnopqrstuvwxyz":
                charList[i] = c
                newWord = "".join(charList)
                # skip if the character is same as original or if the word is not present in the wordSet
                if c == oldChar or newWord not in wordSet:
                    continue
                neighbors.append(newWord)
            charList[i] = oldChar
        return neighbors

    def backtrack(self, source: str, destination: str):
        # store the path if we reached the endWord
        if source == destination:
            tempPath = self.currPath.copy()
            tempPath.reverse()
            self.shortestPaths.append(tempPath)

        if source not in self.adjList:
            return

        for neighbor in self.adjList[source]:
            self.currPath.append(neighbor)
            self.backtrack(neighbor, destination)
            self.currPath.pop()

    def bfs(self, beginWord: str, endWord: str, wordSet: Set[str]):
        q: Deque[str] = deque([beginWord])
        # remove the root word which is the first layer in the BFS
        wordSet.discard(
            beginWord
        )  # discard does nothing if element is not found
        isEnqueued: Dict[str, bool] = {beginWord: True}
        while q:
            # visited will store the words of current layer
            visited: List[str] = []
            for _ in range(len(q)):
                currWord = q.popleft()
                # findNeighbors will have the adjacent words of the currWord
                neighbors = self.findNeighbors(currWord, wordSet)
                for neighbor in neighbors:
                    visited.append(neighbor)
                    if neighbor not in self.adjList:
                        self.adjList[neighbor] = []
                    # add the edge from neighbor to currWord in the list
                    self.adjList[neighbor].append(currWord)
                    if neighbor not in isEnqueued:
                        q.append(neighbor)
                        isEnqueued[neighbor] = True
            # removing the words of the previous layer
            for word in visited:
                wordSet.discard(word)

    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        wordSet: Set[str] = set(
            wordList
        )  # Use a set for efficient removal and checks
        # build the DAG using BFS
        self.bfs(beginWord, endWord, wordSet)

        # every path will start from the endWord
        self.currPath = [endWord]
        # traverse the DAG to find all the paths between endWord and beginWord
        self.backtrack(endWord, beginWord)

        return self.shortestPaths
        
# class Solution:
#     """ 
#     Approach 2: Bidirectional Breadth-First Search (BFS)
#       + Backtracking (Time Limit Exceeded) O(N K^2 + alpha), O(N K)
#     """
#     def __init__(self):
#         self.adjList = {}
#         self.currPath = []
#         self.shortestPaths = []

#     def findNeighbors(self, word, wordList):
#         neighbors = []
#         charList = list(word)
#         for i in range(len(word)):
#             oldChar = charList[i]
#             for ch in range(97, 123):
#                 c = chr(ch)
#                 charList[i] = c
#                 if c == oldChar or "".join(charList) not in wordList:
#                     continue
#                 neighbors.append("".join(charList))
#             charList[i] = oldChar
#         return neighbors

#     def backtrack(self, source, destination):
#         if source == destination:
#             tempPath = list(self.currPath)
#             self.shortestPaths.append(tempPath)
#         for i in range(len(self.adjList.get(source, []))):
#             self.currPath.append(self.adjList[source][i])
#             self.backtrack(self.adjList[source][i], destination)
#             self.currPath.pop()

#     def addEdge(self, word1, word2, direction):
#         if direction == 1:
#             self.adjList[word1] = self.adjList.get(word1, []) + [word2]
#         else:
#             self.adjList[word2] = self.adjList.get(word2, []) + [word1]

#     def bfs(self, beginWord, endWord, wordList):
#         if endWord not in wordList:
#             return False
#         if beginWord in wordList:
#             wordList.remove(beginWord)
#         forwardQueue = set([beginWord])
#         backwardQueue = set([endWord])
#         found = False
#         direction = 1
#         while len(forwardQueue) != 0:
#             visited = set()
#             if len(forwardQueue) > len(backwardQueue):
#                 forwardQueue, backwardQueue = backwardQueue, forwardQueue
#                 direction ^= 1
#             for currWord in forwardQueue:
#                 neighbors = self.findNeighbors(currWord, wordList)
#                 for word in neighbors:
#                     if word in backwardQueue:
#                         found = True
#                         self.addEdge(currWord, word, direction)
#                     elif (
#                         not found
#                         and word in wordList
#                         and word not in forwardQueue
#                     ):
#                         visited.add(word)
#                         self.addEdge(currWord, word, direction)
#             for currWord in forwardQueue:
#                 if currWord in wordList:
#                     wordList.remove(currWord)
#             if found:
#                 break
#             forwardQueue = visited
#         return found

#     def findLadders(self, beginWord, endWord, wordList):
#         copiedWordList = set(wordList)
#         sequence_found = self.bfs(beginWord, endWord, copiedWordList)
#         if sequence_found == False:
#             return self.shortestPaths
#         self.currPath.append(beginWord)
#         self.backtrack(beginWord, endWord)
#         return self.shortestPaths

# @lc code=end

