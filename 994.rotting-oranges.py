#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """ Approach 1: Breadth-First Search (BFS) O(NM), O(NM)"""
        queue = deque()

        fresh_oranges = 0
        n_rows, n_cols = len(grid), len(grid[0])
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        queue.append((-1, -1))

        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes_elapsed += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if n_rows > neighbor_row >= 0 and n_cols > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            queue.append((neighbor_row, neighbor_col))

        return minutes_elapsed if fresh_oranges == 0 else -1
    
    # def orangesRotting(self, grid: List[List[int]]) -> int:
        # """ Approach 2: In-place BFS O(N^2 M^2), O(1) """
    #     queue = deque()

    #     # Step 1). build the initial set of rotten oranges
    #     fresh_oranges = 0
    #     ROWS, COLS = len(grid), len(grid[0])
    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if grid[r][c] == 2:
    #                 queue.append((r, c))
    #             elif grid[r][c] == 1:
    #                 fresh_oranges += 1

    #     # Mark the round / level, _i.e_ the ticker of timestamp
    #     queue.append((-1, -1))

    #     # Step 2). start the rotting process via BFS
    #     minutes_elapsed = -1
    #     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    #     while queue:
    #         row, col = queue.popleft()
    #         if row == -1:
    #             # We finish one round of processing
    #             minutes_elapsed += 1
    #             if queue:  # to avoid the endless loop
    #                 queue.append((-1, -1))
    #         else:
    #             # this is a rotten orange
    #             # then it would contaminate its neighbors
    #             for d in directions:
    #                 neighbor_row, neighbor_col = row + d[0], col + d[1]
    #                 if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
    #                     if grid[neighbor_row][neighbor_col] == 1:
    #                         # this orange would be contaminated
    #                         grid[neighbor_row][neighbor_col] = 2
    #                         fresh_oranges -= 1
    #                         # this orange would then contaminate other oranges
    #                         queue.append((neighbor_row, neighbor_col))

    #     # return elapsed minutes if no fresh orange left
    #     return minutes_elapsed if fresh_oranges == 0 else -1
        
# @lc code=end

