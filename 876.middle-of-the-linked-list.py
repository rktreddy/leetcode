#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head == None:
        #     return head
        # slow = fast = head
        # while fast != None:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow.next
    
        # """ Approach 1: Output to Array O(N), O(N)"""
        # arr = [head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # return arr[len(arr) // 2]
    
        # """ Approach 2: Fast and Slow Pointer O(N), O(1)"""
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
    
        """ Practice: Approach 2: Fast and Slow Pointer O(N), O(1)"""
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# @lc code=end

