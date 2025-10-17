#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # """ Approach 1: Flattening the BST O(N), O(N) """
    # def __init__(self, root: TreeNode):

    #     # Array containing all the nodes in the sorted order
    #     self.nodes_sorted = []

    #     # Pointer to the next smallest element in the BST
    #     self.index = -1

    #     # Call to flatten the input binary search tree
    #     self._inorder(root)

    # def _inorder(self, root: TreeNode) -> None:
    #     if not root:
    #         return
    #     self._inorder(root.left)
    #     self.nodes_sorted.append(root.val)
    #     self._inorder(root.right)

    # def next(self) -> int:
    #     """
    #     @return the next smallest number
    #     """
    #     self.index += 1
    #     return self.nodes_sorted[self.index]

    # def hasNext(self) -> bool:
    #     """
    #     @return whether we have a next smallest number
    #     """
    #     return self.index + 1 < len(self.nodes_sorted)
        
    
    # """ Approach 2: Controlled Recursion O(N), O(N) """
    # def __init__(self, root: TreeNode) -> None:

    #     # Stack for the recursion simulation
    #     self.stack = []

    #     # Remember that the algorithm starts with a call to the helper function
    #     # with the root node as the input
    #     self._leftmost_inorder(root)

    # def _leftmost_inorder(self, root: TreeNode) -> None:

    #     # For a given node, add all the elements in the leftmost branch of the tree
    #     # under it to the stack.
    #     while root:
    #         self.stack.append(root)
    #         root = root.left

    # def next(self) -> int:
    #     """
    #     @return the next smallest number
    #     """
    #     # Node at the top of the stack is the next smallest element
    #     topmost_node = self.stack.pop()

    #     # Need to maintain the invariant. If the node has a right child, call the
    #     # helper function for the right child
    #     if topmost_node.right:
    #         self._leftmost_inorder(topmost_node.right)
    #     return topmost_node.val

    # def hasNext(self) -> bool:
    #     """
    #     @return whether we have a next smallest number
    #     """
    #     return len(self.stack) > 0
    

    """ practice: Approach 2: Controlled Recursion O(N), O(N) """
    # def __init__(self, root: Optional[TreeNode]):
    #     self.stack = []
    #     self._leftmost_inorder(root)

    # def _leftmost_inorder(self, node):
    #     while node:
    #         self.stack.append(node)
    #         node = node.left
        
    # def next(self) -> int:
    #     topmost_node = self.stack.pop()
    #     if topmost_node.right:
    #         self._leftmost_inorder(topmost_node.right)
    #     return topmost_node.val

    # def hasNext(self) -> bool:
    #     return len(self.stack) > 0
    
    # """ Neetcode: Approach 2: Controlled Recursion O(N), O(N) """
    # def __init__(self, root: Optional[TreeNode]):
    #     self.stack = []
    #     while root:
    #         self.stack.append(root)
    #         root = root.left

    # def next(self) -> int:
    #     topmost_node = self.stack.pop()
    #     cur = topmost_node.right
    #     while cur:
    #         self.stack.append(cur)
    #         cur = cur.left
    #     return topmost_node.val

    # def hasNext(self) -> bool:
    #     return self.stack != []

    """ practice: Neetcode: Approach 2: Controlled Recursion O(N), O(N) """
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        topmost_node = self.stack.pop()
        cur = topmost_node.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return topmost_node.val

    def hasNext(self) -> bool:
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

