#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     """ Approach 1: Inorder Traversal + Recursive Construction O(N), O(N) """
    #     # Create a list to store the inorder traversal of the BST
    #     inorder = []
    #     self.inorder_traversal(root, inorder)

    #     # Construct and return the balanced BST
    #     return self.create_balanced_bst(inorder, 0, len(inorder) - 1)

    # def inorder_traversal(self, root: TreeNode, inorder: list):
    #     # Perform an inorder traversal to store the elements in sorted order
    #     if not root:
    #         return
    #     self.inorder_traversal(root.left, inorder)
    #     inorder.append(root.val)
    #     self.inorder_traversal(root.right, inorder)

    # def create_balanced_bst(
    #     self, inorder: list, start: int, end: int
    # ) -> TreeNode:
    #     # Base case: if the start index is greater than the end index, return None
    #     if start > end:
    #         return None

    #     # Find the middle element of the current range
    #     mid = start + (end - start) // 2

    #     # Recursively construct the left and right subtrees
    #     left_subtree = self.create_balanced_bst(inorder, start, mid - 1)
    #     right_subtree = self.create_balanced_bst(inorder, mid + 1, end)

    #     # Create a new node with the middle element and attach the subtrees
    #     node = TreeNode(inorder[mid], left_subtree, right_subtree)
    #     return node
    
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ Approach 2: Day-Stout-Warren Algorithm / In-Place Balancing O(N), O(N) """
        
        if not root:
            return None

        # Step 1: Create the backbone (vine)
        # Temporary dummy node
        vine_head = TreeNode(0)
        vine_head.right = root
        current = vine_head
        while current.right:
            if current.right.left:
                self.right_rotate(current, current.right)
            else:
                current = current.right

        # Step 2: Count the nodes
        node_count = 0
        current = vine_head.right
        while current:
            node_count += 1
            current = current.right

        # Step 3: Create a balanced BST
        m = 2 ** math.floor(math.log2(node_count + 1)) - 1
        self.make_rotations(vine_head, node_count - m)
        while m > 1:
            m //= 2
            self.make_rotations(vine_head, m)

        balanced_root = vine_head.right
        # Delete the temporary dummy node
        vine_head = None
        return balanced_root

    # Function to perform a right rotation
    def right_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        parent.right = tmp

    # Function to perform a left rotation
    def left_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        parent.right = tmp

    # Function to perform a series of left rotations to balance the vine
    def make_rotations(self, vine_head: TreeNode, count: int):
        current = vine_head
        for _ in range(count):
            tmp = current.right
            self.left_rotate(current, tmp)
            current = current.right


# @lc code=end

