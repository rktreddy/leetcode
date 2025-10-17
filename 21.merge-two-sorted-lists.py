#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # iterative approach O(m + n), O(n)
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     dummpy = cur = ListNode()
    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             cur.next = list1
    #             list1 = list1.next
    #         else:
    #             cur.next = list2
    #             list2 = list2.next 
    #         cur = cur.next
    #     cur.next = list1 or list2
    #     return dummpy.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ practice: iterative approach O(m + n), O(n) """
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

    # recuresive approach O(m + n), O(m + n)
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if not list1 or not list2:
    #         return list1 or list2
    #     if list1.val < list2.val:
    #         list1.next = self.mergeTwoLists(list1.next, list2)
    #         return list1
    #     else:
    #         list2.next = self.mergeTwoLists(list1, list2.next)
    #         return list2
        
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     """ practice: recuresive approach O(m + n), O(m + n) """
    #     if not list1 or not list2:
    #         return list1 or list2
    #     if list1.val < list2.val:
    #         list1.next = self.mergeTwoLists(list1.next, list2)
    #         return list1
    #     else:
    #         list2.next = self.mergeTwoLists(list1, list2.next)
    #         return list2
        
    # # in-place, recursive approach
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if None in (list1, list2):
    #         return list1 or list2
        
    #     dummy = cur = ListNode()
    #     dummy.next = list1
    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             list1 = list1.next
    #         else:
    #             nxt = cur.next
    #             cur.next = list2
    #             tmp = list2.next
    #             list2.next = nxt
    #             list2 = tmp
    #         cur = cur.next
    #     cur.next = list1 or list2
    #     return dummy.next

# @lc code=end

