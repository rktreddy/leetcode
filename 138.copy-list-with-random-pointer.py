#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # def __init__(self) -> None:
    #     self.visitedHash = {}

    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     """ Approach 1: Recursive O(N), O(N) """

    #     if head == None:
    #         return None 
        
    #     if head in self.visitedHash:
    #         return self.visitedHash[head]
        
    #     node = Node(head.val, None, None)

    #     self.visitedHash[head] = node

    #     node.next = self.copyRandomList(head.next)
    #     node.random = self.copyRandomList(head.random)

    #     return node 


    # def __init__(self) -> None:
    #     self.visited = {}
        

    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     """ practice: Approach 1: Recursive O(N), O(N) """
    #     if not head:
    #         return None
        
    #     if head in self.visited:
    #         return self.visited[head]
        
    #     node = Node(head.val, None, None)
    #     self.visited[head] = node

    #     node.next = self.copyRandomList(head.next)
    #     node.random = self.copyRandomList(head.random)

    #     return node

    def __init__(self) -> None:
        self.visited = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """ practice: Approach 1: Recursive O(N), O(N) """
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val, None, None)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
      
    # """ Approach 2: Iterative with O(N) Space: O(N), O(N)"""
    # def __init__(self) -> None:
    #     self.visited = {}

    # def getClonedNode(self, node): 
    #     if node:
    #         if node in self.visited:
    #             return self.visited[node]
    #         else:
    #             self.visited[node ] = Node(node.val, None, None)
    #             return self.visited[node]
    #     return None 
    
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     if not head:
    #         return head
        
    #     old_node = head
    #     new_node = Node(old_node.val, None, None)
    #     self.visited[old_node] = new_node
    #     while old_node != None:
    #         new_node.random = self.getClonedNode(old_node.random)
    #         new_node.next = self.getClonedNode(old_node.next)

    #         old_node = old_node.next
    #         new_node = new_node.next

    #     return self.visited[head]
    
    # """ Approach 3: Iterative with O(1) Space : O(N), O(1)"""
    # def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
    #     if not head:
    #         return head

    #     # Creating a new weaved list of original and copied nodes.
    #     ptr = head
    #     while ptr:

    #         # Cloned node
    #         new_node = Node(ptr.val, None, None)

    #         # Inserting the cloned node just next to the original node.
    #         # If A->B->C is the original linked list,
    #         # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
    #         new_node.next = ptr.next
    #         ptr.next = new_node
    #         ptr = new_node.next

    #     ptr = head

    #     # Now link the random pointers of the new nodes created.
    #     # Iterate the newly created list and use the original nodes random pointers,
    #     # to assign references to random pointers for cloned nodes.
    #     while ptr:
    #         ptr.next.random = ptr.random.next if ptr.random else None
    #         ptr = ptr.next.next

    #     # Unweave the linked list to get back the original linked list and the cloned list.
    #     # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
    #     ptr_old_list = head  # A->B->C
    #     ptr_new_list = head.next  # A'->B'->C'
    #     head_new = head.next
    #     while ptr_old_list:
    #         ptr_old_list.next = ptr_old_list.next.next
    #         ptr_new_list.next = (
    #             ptr_new_list.next.next if ptr_new_list.next else None
    #         )
    #         ptr_old_list = ptr_old_list.next
    #         ptr_new_list = ptr_new_list.next
    #     return head_new

# """ Neetcode solutions """
# class Solution:
    # def __init__(self):
    #     self.map = {}

    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     """ Neetcode: 1. Hash Map (Recursion) O(n), O(n)"""
    #     if head is None:
    #         return None
    #     if head in self.map:
    #         return self.map[head]
        
    #     copy = Node(head.val)
    #     self.map[head] = copy
    #     copy.next = self.copyRandomList(head.next)
    #     copy.random = self.map.get(head.random)
    #     return copy
   
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     """ 2. Hash Map (Two Pass) O(n), O(n) """
    #     oldToCopy = {None: None}

    #     cur = head
    #     while cur:
    #         copy = Node(cur.val)
    #         oldToCopy[cur] = copy
    #         cur = cur.next
    #     cur = head
    #     while cur:
    #         copy = oldToCopy[cur]
    #         copy.next = oldToCopy[cur.next]
    #         copy.random = oldToCopy[cur.random]
    #         cur = cur.next
    #     return oldToCopy[head]
    
    
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     """ 3. Hash Map (One Pass) O(n), O(n) """
    #     oldToCopy = collections.defaultdict(lambda: Node(0))
    #     oldToCopy[None] = None
        
    #     cur = head
    #     while cur:
    #         oldToCopy[cur].val = cur.val
    #         oldToCopy[cur].next = oldToCopy[cur.next]
    #         oldToCopy[cur].random = oldToCopy[cur.random]
    #         cur = cur.next
    #     return oldToCopy[head]
    
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     """ 4. Space Optimized - I O(n), o(1) """
    #     if head is None:
    #         return None
        
    #     l1 = head
    #     while l1 is not None:
    #         l2 = Node(l1.val)
    #         l2.next = l1.next
    #         l1.next = l2
    #         l1 = l2.next
            
    #     newHead = head.next
        
    #     l1 = head
    #     while l1 is not None:
    #         if l1.random is not None:
    #             l1.next.random = l1.random.next
    #         l1 = l1.next.next
            
    #     l1 = head
    #     while l1 is not None:
    #         l2 = l1.next
    #         l1.next = l2.next
    #         if l2.next is not None:
    #             l2.next = l2.next.next
    #         l1 = l1.next
            
    #     return newHead
    
    
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     """ 5. Space Optimized - II o(n), O(1) """
    #     if head is None:
    #         return None

    #     l1 = head
    #     while l1:
    #         l2 = Node(l1.val)
    #         l2.next = l1.random
    #         l1.random = l2
    #         l1 = l1.next
        
    #     newHead = head.random
        
    #     l1 = head
    #     while l1:
    #         l2 = l1.random
    #         l2.random = l2.next.random if l2.next else None
    #         l1 = l1.next
            
    #     l1 = head
    #     while l1 is not None:
    #         l2 = l1.random
    #         l1.random = l2.next
    #         l2.next = l1.next.random if l1.next else None
    #         l1 = l1.next

    #     return newHead
        
# @lc code=end

