#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    # """ Approach 1: Stack of Value/ Minimum Pairs O(1), O(n) """

    # def __init__(self):
    #     self.stack = []
        

    # def push(self, val: int) -> None:
    #     if not self.stack:
    #         self.stack.append((val, val))
    #         return
    #     curr_min = self.stack[-1][1]
    #     self.stack.append((val, min(val, curr_min)))

    # def pop(self) -> None:
    #     self.stack.pop()
        

    # def top(self) -> int:
    #     return self.stack[-1][0]
        
    # def getMin(self) -> int:
    #     return self.stack[-1][1]

    # """ Approach 2: Two Stacks O(1), O(n) """
    # def __init__(self) -> None:
    #     self.stack = []
    #     self.min_stack = []

    # def push(self, val: int) -> None:     
    #     self.stack.append(val)   
    #     if not self.min_stack or self.stack[-1] <= self.min_stack[-1]:
    #         self.min_stack.append(val)
        

    # def pop(self) -> None:
    #     if self.stack[-1] == self.min_stack[-1]:
    #         self.min_stack.pop()
    #     self.stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]
    
    # def getMin(self) -> int:
    #     return self.min_stack[-1]

    """ Approach 3: Improved Two Stacks O(1), O(n)"""
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:

        # We always put the number onto the main stack.
        self.stack.append(x)

        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])

        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:

        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

        # And like before, pop the top of the main stack.
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

