#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    #     """ Approach 1: Recursion (Postorder Traversal) O(n), O(n) """
    #     to_delete_set = set(to_delete)
    #     forest = []

    #     root = self._process_node(root, to_delete_set, forest)

    #     # If the root is not deleted, add it to the forest
    #     if root:
    #         forest.append(root)

    #     return forest

    # def _process_node(
    #     self, node: TreeNode, to_delete_set: Set[int], forest: List[TreeNode]
    # ) -> TreeNode:
    #     if not node:
    #         return None

    #     node.left = self._process_node(node.left, to_delete_set, forest)
    #     node.right = self._process_node(node.right, to_delete_set, forest)

    #     # Node Evaluation: Check if the current node needs to be deleted
    #     if node.val in to_delete_set:
    #         # If the node has left or right children, add them to the forest
    #         if node.left:
    #             forest.append(node.left)
    #         if node.right:
    #             forest.append(node.right)
    #         # Delete the current node by returning None to its parent
    #         return None

    #     return node
    

#    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
#         """ Approach 2: BFS Forest Formation O(n), O(n) """
    
#         if not root:
#             return []

#         to_delete_set = set(to_delete)
#         forest = []

#         nodes_queue = deque([root])

#         while nodes_queue:
#             current_node = nodes_queue.popleft()

#             if current_node.left:
#                 nodes_queue.append(current_node.left)
#                 # Disconnect the left child if it needs to be deleted
#                 if current_node.left.val in to_delete_set:
#                     current_node.left = None

#             if current_node.right:
#                 nodes_queue.append(current_node.right)
#                 # Disconnect the right child if it needs to be deleted
#                 if current_node.right.val in to_delete_set:
#                     current_node.right = None

#             # If the current node needs to be deleted, add its non-null children to the forest
#             if current_node.val in to_delete_set:
#                 if current_node.left:
#                     forest.append(current_node.left)
#                 if current_node.right:
#                     forest.append(current_node.right)

#         # Ensure the root is added to the forest if it is not to be deleted
#         if root.val not in to_delete_set:
#             forest.append(root)

#         return forest
   
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """ practice: Approach 2: BFS Forest Formation O(n), O(n) """
        if not root:
            return []
        to_delete_set = set(to_delete)
        forest = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                if node.left.val in to_delete_set:
                    node.left = None

            if node.right:
                queue.append(node.right)
                if node.right.val in to_delete_set:
                    node.right = None

            if node.val in to_delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)

        if root.val not in to_delete_set:
            forest.append(root)
        return forest

                
            
   
#    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
#         """ Approach 2: BFS Forest Formation O(n), O(n) """
   
        
# @lc code=end

