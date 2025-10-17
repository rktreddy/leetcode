#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     """ Approach 1: Breadth-first Search (BFS), Overwriting Input O(N), O(N) N cells """
        
    #     max_row = len(grid) - 1
    #     max_col = len(grid[0]) - 1
    #     directions = [
    #         (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
    #     # Helper function to find the neighbors of a given cell.
    #     def get_neighbours(row, col):
    #         for row_difference, col_difference in directions:
    #             new_row = row + row_difference
    #             new_col = col + col_difference
    #             if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
    #                 continue
    #             if grid[new_row][new_col] != 0:
    #                 continue
    #             yield (new_row, new_col)
        
    #     # Check that the first and last cells are open. 
    #     if grid[0][0] != 0 or grid[max_row][max_col] != 0:
    #         return -1
        
    #     # Set up the BFS.
    #     queue = deque()
    #     queue.append((0, 0))
    #     grid[0][0] = 1 
        
    #     # Carry out the BFS.
    #     while queue:
    #         row, col = queue.popleft()
    #         distance = grid[row][col]
    #         if (row, col) == (max_row, max_col):
    #             return distance
    #         for neighbour_row, neighbour_col in get_neighbours(row, col):
    #             grid[neighbour_row][neighbour_col] = distance + 1
    #             queue.append((neighbour_row, neighbour_col))
        
    #     # There was no path.
    #     return -1

    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     """ Approach 2: Breadth-first Search (Without Overwriting the Input) O(N), O(N) """
    #     """ Distances on queue """
    #     max_row = len(grid) - 1
    #     max_col = len(grid[0]) - 1
    #     directions = [
    #         (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
    #     # Helper function to find the neighbors of a given cell.
    #     def get_neighbours(row, col):
    #         for row_difference, col_difference in directions:
    #             new_row = row + row_difference
    #             new_col = col + col_difference
    #             if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
    #                 continue
    #             if grid[new_row][new_col] != 0:
    #                 continue
    #             yield (new_row, new_col)
        
    #     # Check that the first and last cells are open. 
    #     if grid[0][0] != 0 or grid[max_row][max_col] != 0:
    #         return -1
        
    #     # Set up the BFS.
    #     queue = deque([(0, 0, 1)])
    #     visited = {(0, 0)}
        
    #     # Do the BFS.
    #     while queue:
    #         row, col, distance = queue.popleft()
    #         if (row, col) == (max_row, max_col):
    #             return distance
    #         for neighbour in get_neighbours(row, col):
    #             if neighbour in visited:
    #                 continue
    #             visited.add(neighbour)
    #             # Note that the * splits neighbour into its values.
    #             queue.append((*neighbour, distance + 1))
                
    #     # There was no path.
    #     return -1

    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     """ Approach 2: Breadth-first Search (Without Overwriting the Input) O(N), O(N) """
    #     """ Starting a new collection for each distance """
        
    #     max_row = len(grid) - 1
    #     max_col = len(grid[0]) - 1
    #     directions = [
    #         (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
    #     # Helper function to find the neighbors of a given cell.
    #     def get_neighbours(row, col):
    #         for row_difference, col_difference in directions:
    #             new_row = row + row_difference
    #             new_col = col + col_difference
    #             if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
    #                 continue
    #             if grid[new_row][new_col] != 0:
    #                 continue
    #             yield (new_row, new_col)
        
    #     # Check that the first and last cells are open. 
    #     if grid[0][0] != 0 or grid[max_row][max_col] != 0:
    #         return -1
        
    #     # Set up the BFS.
    #     current_layer = [(0, 0)]
    #     next_layer = []
    #     visited = {(0, 0)}
    #     current_distance = 1
        
    #     while current_layer:
            
    #         # Process the current layer.
    #         for row, col in current_layer:
    #             if (row, col) == (max_row, max_col):
    #                 return current_distance
    #             for neighbour in get_neighbours(row, col):
    #                 if neighbour in visited:
    #                     continue
    #                 visited.add(neighbour)
    #                 next_layer.append(neighbour)
            
    #         # Set up for processing the next layer.
    #         current_distance += 1
    #         current_layer = next_layer
    #         next_layer = []
                
    #     # There was no path.
    #     return -1
    
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     """ Approach 2: Breadth-first Search (Without Overwriting the Input) O(N), O(N) """
    #     """ Keeping track of how many cells at each distance are on the queue """
        
    #     max_row = len(grid) - 1
    #     max_col = len(grid[0]) - 1
    #     directions = [
    #         (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
    #     # Helper function to find the neighbors of a given cell.
    #     def get_neighbours(row, col):
    #         for row_difference, col_difference in directions:
    #             new_row = row + row_difference
    #             new_col = col + col_difference
    #             if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
    #                 continue
    #             if grid[new_row][new_col] != 0:
    #                 continue
    #             yield (new_row, new_col)
        
    #     # Check that the first and last cells are open. 
    #     if grid[0][0] != 0 or grid[max_row][max_col] != 0:
    #         return -1
        
    #     # Set up the BFS.
    #     queue = deque([(0, 0)])
    #     visited = {(0, 0)}
    #     current_distance = 1
        
    #     # Do the BFS.
    #     while queue:
    #         # Process all nodes at current_distance from the top-left cell.
    #         nodes_of_current_distance = len(queue)
    #         for _ in range(nodes_of_current_distance):
    #             row, col = queue.popleft()
    #             if (row, col) == (max_row, max_col):
    #                 return current_distance
    #             for neighbour in get_neighbours(row, col):
    #                 if neighbour in visited:
    #                     continue
    #                 visited.add(neighbour)
    #                 queue.append(neighbour)
    #         # We'll now be processing all nodes at current_distance + 1
    #         current_distance += 1
                    
    #     # There was no path.
    #     return -1 
    
    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     """ Approach 3: A* (Advanced) O(N), O(N) """
        
    #     max_row = len(grid) - 1
    #     max_col = len(grid[0]) - 1
    #     directions = [
    #         (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
    #     # Helper function to find the neighbors of a given cell.
    #     def get_neighbours(row, col):
    #         for row_difference, col_difference in directions:
    #             new_row = row + row_difference
    #             new_col = col + col_difference
    #             if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
    #                 continue
    #             if grid[new_row][new_col] != 0:
    #                 continue
    #             yield (new_row, new_col)
        
    #     # Helper function for the A* heuristic.
    #     def best_case_estimate(row, col):
    #         return max(max_row - row, max_col - col)
            
    #     # Check that the first and last cells are open. 
    #     if grid[0][0] or grid[max_row][max_col]:
    #         return -1
        
    #     # Set up the A* search.
    #     visited = set()
    #     # Entries on the priority queue are of the form
    #     # (total distance estimate, distance so far, (cell row, cell col))
    #     priority_queue = [(1 + best_case_estimate(0, 0), 1, (0, 0))]
    #     while priority_queue:
    #         estimate, distance, cell = heapq.heappop(priority_queue)
    #         if cell in visited:
    #             continue
    #         if cell == (max_row, max_col):
    #             return distance
    #         visited.add(cell)
    #         for neighbour in get_neighbours(*cell):
    #             # The check here isn't necessary for correctness, but it
    #             # leads to a substantial performance gain.
    #             if neighbour in visited:
    #                 continue
    #             estimate = best_case_estimate(*neighbour) + distance + 1
    #             entry = (estimate, distance + 1, neighbour)
    #             heapq.heappush(priority_queue, entry)
        
    #     # There was no path.
    #     return -1

    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     """ Neetcode solution (BFS) O(N^2), O(N^2)?? """
    #     N = len(grid)
    #     queue = deque([(0, 0, 1)]) # r, c, length
    #     visited = set((0, 0))
    #     # directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
    #     #           [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
    #     directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
    #                   (0, 1), (1, -1), (1, 0), (1, 1)]

    #     while queue:
    #         r, c, length = queue.popleft()
    #         if min(r, c) < 0 or max(r, c) >= N or grid[r][c]:
    #             continue
    #         if r == N - 1 and c == N - 1:
    #             return length
            
    #         for dr, dc in directions:
    #             if (r + dr, c + dc) not in visited:
    #                 queue.append((r + dr, c + dc, length + 1))
    #                 visited.add((r + dr, c + dc))

    #     return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """ practice: Neetcode solution (BFS) O(N^2), O(N^2) N = len(grid) """
        n = len(grid)
        queue = deque([(0, 0, 1)]) # r, c, length
        visited = set((0, 0)) # r, c

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        
        while queue:
            r, c, length = queue.popleft()
            if min(r, c) < 0 or max(r, c) >= n or grid[r][c]:
                continue
            if r == n - 1 and c == n - 1:
                return length
            
            for dr, dc in directions:
                if (r + dr, c + dc) not in visited:
                    queue.append((r + dr, c + dc, length + 1))
                    visited.add((r + dr, c + dc))
        return -1 

# @lc code=end

