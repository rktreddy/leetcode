#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     """ cracking faang: linked list O(n), O(1) """
    #     if not head:
    #         return None
    #     odd = head
    #     even_head = even = head.next
    #     while even and even.next:
    #         odd.next = odd.next.next
    #         odd = odd.next

    #         even.next = even.next.next
    #         even = even.next
        
    #     odd.next = even_head
    #     return head
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ practice: cracking faang: linked list O(n), O(1)"""
        if not head:
            return None
        odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head
        
# @lc code=end

