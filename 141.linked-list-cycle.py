#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     """ My solution"""
    #     hashset = set()
    #     current = head
    #     while current is not None:
    #         if current in hashset:
    #             return True
    #         hashset.add(current)

    #         if current.next is None:
    #             return False
            
    #         current = current.next

    
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     """ Fast python slow and fast traversal"""
    #     try:
    #         slow = head
    #         fast = head.next
    #         while slow is not fast:
    #             slow = slow.next
    #             fast = fast.next.next
    #         return True
    #     except:
    #         return False    
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True            
        return False

# @lc code=end

