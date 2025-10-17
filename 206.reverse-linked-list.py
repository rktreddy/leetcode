#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # """ Approach 1: Iterative O(n), O(1) """
        # prev = None
        # curr = head

        # while curr:
        #     next_temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_temp
        
        # return prev
    
        """ practice: Approach 1: Iterative O(n), O(1) """
        prev = None 
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp

        return prev

        
        # """ Approach 2: Recursive O(n), O(n) """
        # if (not head) or (not head.next):
        #     return head
        
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p
    
# @lc code=end

