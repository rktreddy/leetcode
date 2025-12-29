#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    # def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     """ Approach 1: DFS by Recursion O(N), O(N) """

    #     if not head:
    #         return head

    #     # pseudo head to ensure the `prev` pointer is never none
    #     pseudoHead = Node(None, None, head, None)
    #     self.flatten_dfs(pseudoHead, head)

    #     # detach the pseudo head from the real head
    #     pseudoHead.next.prev = None
    #     return pseudoHead.next


    # def flatten_dfs(self, prev, curr):
    #     """ return the tail of the flatten list """
    #     if not curr:
    #         return prev

    #     curr.prev = prev
    #     prev.next = curr

    #     # the curr.next would be tempered in the recursive function
    #     tempNext = curr.next
    #     tail = self.flatten_dfs(curr, curr.child)
    #     curr.child = None
    #     return self.flatten_dfs(tail, tempNext)
    
   
    def flatten(self, head):
        """ Approach 2: DFS by Iteration  O(N), O(N) """
        if not head:
            return

        pseudoHead = Node(0,None,head,None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
 
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next

        
# @lc code=end

