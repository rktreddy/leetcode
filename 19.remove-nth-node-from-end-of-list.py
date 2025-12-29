#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     """ Approach 1: Two pass algorithm O(L), O(1) """
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     length = 0
    #     first = head
    #     while first is not None:
    #         length += 1
    #         first = first.next
    #     length -= n
    #     first = dummy
    #     while length > 0:
    #         length -= 1
    #         first = first.next
    #     first.next = first.next.next
    #     return dummy.next
    
    # def removeNthFromEnd(self, head, n):
    #     """ Approach 2: One pass algorithm O(L), O(1) """
    #     """
    #     :type head: ListNode
    #     :type n: int
    #     :rtype: ListNode
    #     """
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     first = dummy
    #     second = dummy
    #     # Advances first pointer so that the gap between first and second is n nodes apart
    #     for i in range(n + 1):
    #         first = first.next
    #         print(first.val)
    #     # Move first to the end, maintaining the gap
    #     while first is not None:
    #         first = first.next
    #         second = second.next
    #         print(f'first: {first.val}, second: {second.val}')
    #     second.next = second.next.next
    #     return dummy.next
    
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     """ Neetcode Two Pointers O(n), O(1) """
    #     dummy = ListNode(0, head)
    #     left = dummy
    #     right = head

    #     while n > 0:
    #         right = right.next
    #         n -= 1

    #     while right:
    #         left = left.next
    #         right = right.next

    #     # delete
    #     left.next = left.next.next
    #     return dummy.next
    
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     """ practice: Neetcode Two Pointers O(n), O(1) """
    #     dummy = ListNode(0, head)
    #     left = dummy
    #     right = head

    #     while n > 0:
    #         right = right.next
    #         n -= 1

    #     while right:
    #         left = left.next
    #         right = right.next
        
    #     left.next = left.next.next

    #     return dummy.next
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """ practice: Neetcode Two Pointers O(n), O(1) """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left = left.next.next

        return dummy.next

        
# @lc code=end

