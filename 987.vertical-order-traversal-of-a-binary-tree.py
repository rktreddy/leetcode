#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """ Approach 1: BFS/DFS with Global Sorting O(N log N), O(N) """
        # ## BFS Traversal
        # if not root:
        #     return []
        
        # node_list = []

        # def BFS(root):
        #     queue = deque([(root, 0, 0)])
        #     while queue:
        #         node, row, column = queue.popleft()
        #         if node is not None:
        #             node_list.append((column, row, node.val))
        #             queue.append((node.left, row + 1, column - 1))
        #             queue.append((node.right, row + 1, column + 1))

        # # step 1). construct the global node list, with the coordinates
        # BFS(root)

        # # step 2). sort the global node list, according to the coordinates
        # node_list.sort()

        # # step 3). retrieve the sorted results partitioned by the column index
        # ret = OrderedDict()
        # for column, row, value in node_list:
        #     if column in ret:
        #         ret[column].append(value)
        #     else:
        #         ret[column] = [value]
        # return list(ret.values())
    
        # ## DFS Traversal
        # if not root:
        #     return []

        # node_list = []

        # def DFS(node, row, column):
        #     if node is not None:
        #         node_list.append((column, row, node.val))
        #         DFS(node.left, row + 1, column - 1)
        #         DFS(node.right, row + 1, column + 1)
            
        # # step 1). construct the node list, with the coordinates
        # DFS(root, 0, 0)

        # # step 2). sort the node list globally, according to the coordinates
        # node_list.sort()

        # # step 3). retrieve the sorted results grouped by the column index
        # ret = []
        # curr_column_index = node_list[0][0]
        # curr_column = []
        # for column, row, value in node_list:
        #     if column == curr_column_index:
        #         curr_column.append(value)
        #     else:
        #         # end of a column, and start the next column
        #         ret.append(curr_column)
        #         curr_column_index =  column
        #         curr_column = [value]
        # # add the last column
        # ret.append(curr_column)
        # return ret


    # def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """ Approach 2: BFS/DFS with Partition Sorting O(N log N), O(N) """
        # # BFS Traversal
        # if root is None:
        #     return []
        
        # columnTable = defaultdict(list)
        # min_column = max_column = 0

        # def BFS(root):
        #     nonlocal min_column, max_column
        #     queue = deque([(root, 0, 0)])

        #     while queue:
        #         node, row, column = queue.popleft()

        #         if node is not None:
        #             columnTable[column].append((row, node.val))
        #             min_column = min(min_column, column)
        #             max_column = max(max_column, column)

        #             queue.append((node.left, row + 1, column - 1))
        #             queue.append((node.right, row + 1, column + 1))

        # # step 1). BFS traversal
        # BFS(root)

        # # step 2). extract the values from the columnTable
        # ret = []
        # for col in range(min_column, max_column + 1):
        #     # sort first by 'row', then by 'value', in ascending order
        #     ret.append([val for row, val in sorted(columnTable[col])])

        # return ret

        # # DFS tr, 0, 0

    # def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """ Approach 2:  BFS with Partition Sorting  sim to 314 O(N log N), O(N) """

    #     if not root:
    #         return []
        
    #     columnTable = defaultdict(list)
    #     min_column = max_column = 0
    #     queue = deque([(root, 0, 0)])

    #     while queue:
    #         node, row, column = queue.popleft()

    #         if node is not None:
    #             columnTable[column].append((row, node.val))
    #             min_column = min(min_column, column)
    #             max_column = max(max_column, column)

    #             queue.append((node.left, row + 1, column - 1))
    #             queue.append((node.right, row + 1, column + 1))

    #     # ret = []
    #     # for col in range(min_column, max_column + 1):
    #     #     # sort first by 'row', then by 'value', in ascending order
    #     #     ret.append([val for row, val in sorted(columnTable[col])])
        
    #     # return ret 

    #     return [[val for row, val in sorted(columnTable[x])] for x in range(min_column, max_column + 1)]

    # def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """ practice: Approach 2:  BFS with Partition Sorting  sim to 314 O(N log N), O(N) """
        
    #     if not root:
    #         return []

    #     queue = deque([(root, 0, 0)]) # root, row, col
    #     columnTable = defaultdict(list)
    #     min_column = 0
    #     max_column = 0

    #     while queue:
    #         node, row, column = queue.popleft()

    #         if node is not None:
    #             columnTable[column].append((row, node.val))
    #             min_column = min(min_column, column)
    #             max_column = max(max_column, column)

    #             queue.append((node.left, row + 1, column - 1))
    #             queue.append((node.right, row + 1, column + 1))

    #     return [[val for row, val in sorted(columnTable[x])] for x in range(min_column, max_column + 1)]

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ practice: Approach 2:  BFS with Partition Sorting  sim to 314 O(N log N), O(N) """
        if not root:
            return []
        
        queue = deque([(root, 0, 0)])
        columnTable = defaultdict(list)
        min_column, max_column = 0, 0

        while queue:
            node, row, column = queue.popleft()
            if node is not None:
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        return [[val for row, val in sorted(columnTable[x])] for x in range(min_column, max_column + 1)]
   


# @lc code=end

# 314
def verticalOrder(self, root: TreeNode) -> List[List[int]]:
    # practice: Approach 2: BFS without Sorting time O(N) and space O(N)
    if not root:
        return None

    columnTable = defaultdict(list)
    min_column = max_column = 0
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()
        if node is not None:
            columnTable[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))

    return [columnTable[x] for x in range(min_column, max_column + 1)]

