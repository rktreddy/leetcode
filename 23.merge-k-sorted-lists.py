#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class HeapNode:
#     def __init__(self, node) -> None:
#         self.node = node

#     def __lt__(self, other):
#         return self.node.val < other.node.val
    
# practice
# class HeapNode:
#     def __init__(self, node):
#         self.node = node

#     def __lt__(self, other):
#         return self.node.val < other.node.val
        
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     """ Approach 1: Brute Force O(N log N), O(N) """
    #     nodes = []
    #     head = point = ListNode(0)

    #     for l in lists:
    #         while l:
    #             nodes.append(l.val)
    #             l = l.next
        
    #     for x in sorted(nodes):
    #         point.next = ListNode(x)
    #         point = point.next

    #     return head.next
    
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     """ Approach 2: Compare one by one O(k N), O(n) """
    #     """ Approach 3: Optimize Approach 2 by Priority Queue O(n log k), O(n) """
    #     dummy = ListNode(0)
    #     current = dummy
    #     heap = []

    #     for l in lists:
    #         if l:
    #             heapq.heappush(heap, HeapNode(l))

    #     while heap:
    #         heap_node = heapq.heappop(heap)
    #         node = heap_node.node
    #         current.next = node
    #         current = current.next
    #         if node.next:
    #             heapq.heappush(heap, HeapNode(node.next))

    #     return dummy.next

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     """ practice: Approach 3: Optimize Approach 2 by Priority Queue O(n log k), O(n) """

    #     dummy = ListNode(0)
    #     current = dummy
    #     heap = []

    #     for l in lists:
    #         if l:
    #             heapq.heappush(heap, HeapNode(l))

    #     while heap:
    #         heap_node = heapq.heappop(heap)
    #         node = heap_node.node
    #         current.next = node
    #         current = current.next

    #         if node.next:
    #             heapq.heappush(heap, HeapNode(node.next))

    #     return dummy.next
    

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # """ Approach 4: Merge lists one by one O(k N), O(1)"""

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     """ Approach 5: Merge with Divide And Conquer O(N log k), O(1) """
    #     n = len(lists)
    #     interval = 1
    #     while interval < n:
    #         for i in range(0, n - interval, interval * 2):
    #             lists[i] = self.merge2list(lists[i], lists[i + interval])
    #         interval *= 2
    #     return lists[0] if n > 0 else None

    # def merge2list(self, l1, l2):
    #     dummy = ListNode(0)
    #     curr = dummy
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             curr.next = l1
    #             l1 = l1.next
    #         else:
    #             curr.next = l2
    #             l2 = l2.next
    #         curr = curr.next
    #     curr.next = l1 or l2
    #     return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ practice: Approach 5: Merge with Divide And Conquer O(N log k), O(1) """
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.merge2lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if n > 0 else None
    
    def merge2lists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
    
        
# @lc code=end

