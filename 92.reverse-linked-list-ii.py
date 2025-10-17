#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    #     """ Approach 1: Recursion O(N), O(N) """
    #     if not head:
    #         return None

    #     left, right = head, head
    #     stop = False

    #     def recurseAndReverse(right, m, n):
    #         nonlocal left, stop

    #         # base case. Don't proceed any further
    #         if n == 1:
    #             return

    #         # Keep moving the right pointer one step forward until (n == 1)
    #         right = right.next

    #         # Keep moving left pointer to the right until we reach the proper node
    #         # from where the reversal is to start.
    #         if m > 1:
    #             left = left.next

    #         # Recurse with m and n reduced.
    #         recurseAndReverse(right, m - 1, n - 1)

    #         # In case both the pointers cross each other or become equal, we
    #         # stop i.e. don't swap data any further. We are done reversing at this
    #         # point.
    #         if left == right or right.next == left:
    #             stop = True

    #         # Until the boolean stop is false, swap data between the two pointers
    #         if not stop:
    #             left.val, right.val = right.val, left.val

    #             # Move left one step to the right.
    #             # The right pointer moves one step back via backtracking.
    #             left = left.next

    #     recurseAndReverse(right, m, n)
    #     return head
        
    # def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    #     """ Approach 2: Iterative Link Reversal. O(N), O(1) """
    #     # Empty list
    #     if not head:
    #         return None

    #     # Move the two pointers until they reach the proper starting point
    #     # in the list.
    #     cur, prev = head, None
    #     while m > 1:
    #         prev = cur
    #         cur = cur.next
    #         m, n = m - 1, n - 1

    #     # The two pointers that will fix the final connections.
    #     tail, con = cur, prev

    #     # Iteratively reverse the nodes until n becomes 0.
    #     while n:
    #         third = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = third
    #         n -= 1

    #     # Adjust the final connections as explained in the algorithm
    #     if con:
    #         con.next = prev
    #     else:
    #         head = prev
    #     tail.next = cur
    #     return head
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """ Approach 2: Iterative Link Reversal. O(N), O(1)
         https://walkccc.me/LeetCode/problems/92/#__tabbed_2_3 """
        
        if not head and m == n:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(m - 1):
            prev = prev.next  # Point to the node before the sublist [m, n].

        tail = prev.next  # Be the tail of the sublist [m, n].

        # Reverse the sublist [m, n] one by one.
        for _ in range(n - m):
            cache = tail.next
            tail.next = cache.next
            cache.next = prev.next
            prev.next = cache

        return dummy.next
    
# @lc code=end

