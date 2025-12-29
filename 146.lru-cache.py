#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

# class ListNode:
#     def __init__(self, key, val) -> None:
#         self.key = key
#         self.val = val
#         self.next = None
#         self.prev = None

class ListNode:
    """ practice """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:

    # """ Neetcode: Approach 1:bruteforce  o(n), O(n) """
    # def __init__(self, capacity: int):
    #     self.cache = OrderedDict()
    #     self.cap = capacity

    # def get(self, key: int) -> int:
    #     if key not in self.cache:
    #         return -1
    #     self.cache.move_to_end(key)
    #     return self.cache[key]

    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         self.cache.move_to_end(key)
    #     self.cache[key] = value

    #     if len(self.cache) > self.cap:
    #         self.cache.popitem(last=False)


    # """ Approach 1: Doubly Linked List  o(1), O(capacity) """

    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.dic = {}
    #     self.head = ListNode(-1, -1)
    #     self.tail = ListNode(-1, -1)
    #     self.head.next = self.tail
    #     self.tail.prev = self.head

    # def get(self, key: int) -> int:
    #     if key not in self.dic:
    #         return -1
        
    #     node = self.dic[key]
    #     self.remove(node)
    #     self.add(node)
    #     return node.val
        

    # def put(self, key: int, value: int) -> None:
    #     if key in self.dic:
    #         old_node = self.dic[key]
    #         self.remove(old_node)

    #     node = ListNode(key, value)
    #     self.dic[key] = node
    #     self.add(node)
        
    #     if len(self.dic) > self.capacity:
    #         node_to_delete = self.head.next
    #         self.remove(node_to_delete)
    #         del self.dic[node_to_delete.key]

    # def add(self, node):
    #     previous_end = self.tail.prev
    #     previous_end.next = node
    #     node.prev = previous_end
    #     node.next = self.tail
    #     self.tail.prev = node

    # def remove(self, node):
    #     node.prev.next = node.next
    #     node.next.prev = node.prev

    """ practice: Approach 1: Doubly Linked List  o(1), O(capacity) """

    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.cache = {}

    #     self.head = ListNode(-1, -1)
    #     self.tail = ListNode(-1, -1)

    #     self.head.next = self.tail
    #     self.tail.prev = self.head
        
    # def get(self, key: int) -> int:
    #     if key not in self.cache:
    #         return -1
    #     self.remove(self.cache[key])
    #     self.insert(self.cache[key])
    #     return self.cache[key].val
        
    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         self.remove(self.cache[key])

    #     self.cache[key] = ListNode(key, value)
    #     self.insert(self.cache[key])

    #     if len(self.cache) > self.capacity:
    #         lru = self.head.next
    #         self.remove(lru)
    #         del self.cache[lru.key]        

    # def remove(self, node):
    #     node.prev.next = node.next
    #     node.next.prev = node.prev

    # def insert(self, node):
    #     previous_node = self.tail.prev
    #     previous_node.next = node 
    #     node.prev = previous_node
    #     node.next = self.tail
    #     self.tail.prev = node

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head 

        
    def get(self, key):
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

        
    def put(self, key, val):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]        

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert(self, node):
        prev_node = self.tail.prev
        prev_node.next = self.tail.prev = node
        node.next, node.prev = self.tail, prev_node

    
    # """ Approach 2: Built-in O(1), O(capacity) """
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.dic = collections.OrderedDict()     

    # def get(self, key: int) -> int:
    #     if key not in self.dic:
    #         return -1
        
    #     self.dic.move_to_end(key)
    #     return self.dic[key]

    # def put(self, key: int, value: int) -> None:
    #     if key in self.dic:
    #         self.dic.move_to_end(key)

    #     self.dic[key] = value
    #     if len(self.dic) > self.capacity:
    #         self.dic.popitem(False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

