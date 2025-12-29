#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         """ T: O(N), S: O(N) """
#         def flatten(nestedList):
#             items = []
#             for item in nestedList:
#                 if item.isInteger():
#                     items.append(item.getInteger())
#                 else:
#                     items.extend(flatten(item.getList()))
#             return items

#         self.queue = collections.deque(flatten(nestedList))

    
#     def next(self) -> int:
#         return self.queue.popleft() # O(1)
        
    
#     def hasNext(self) -> bool:
#         return len(self.queue) != 0 # O(1)
    
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """ practice: T: O(N), S: O(N) """
        def flatten(nestedList):
            items = []
            for item in nestedList:
                if item.isInteger():
                    items.append(item.getInteger())
                else:
                    items.extend(flatten(item.getList()))
            return items
        
        self.queue = collections.deque(flatten(nestedList))
    
    def next(self) -> int:
        return self.queue.popleft()
    
    def hasNext(self) -> bool:
        return len(self.queue) != 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

