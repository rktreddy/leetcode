#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     """ my first attempt (wrong) """
    #     if not head:
    #         return None 
        
    #     curr, prev = head, None 
    #     while curr:
    #         curr, curr.next = curr.next, curr 
    #         curr = curr.next

    #     return curr
        
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     """ Approach 1: Recursive Approach O(n), O(n) """
    #     if not head or not head.next:
    #         return head
        
    #     first_node = head
    #     second_node = head.next

    #     first_node.next = self.swapPairs(second_node.next)
    #     second_node.next = first_node 

    #     return second_node

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Approach 2: Iterative Approach O(n), O(1) """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy 
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next 

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swa
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next

# @lc code=end

