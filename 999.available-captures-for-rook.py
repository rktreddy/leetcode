#
# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        """ Algomonster: O(m*n), O(1) """
        # Define four directions: up, right, down, left
        # Using pairwise iteration: (-1,0), (0,1), (1,0), (0,-1)
        directions = (-1, 0, 1, 0, -1)
        board_size = len(board)
      
        # Find the rook's position on the board
        for row in range(board_size):
            for col in range(board_size):
                if board[row][col] == "R":
                    captured_pawns = 0
                  
                    # Check all four directions from the rook
                    for i in range(4):
                        # Get direction vector using pairwise
                        dx = directions[i]
                        dy = directions[i + 1]
                      
                        # Start from the rook's adjacent cell in current direction
                        current_row = row + dx
                        current_col = col + dy
                      
                        # Continue moving in the same direction until hitting a boundary or bishop
                        while 0 <= current_row < board_size and 0 <= current_col < board_size and board[current_row][current_col] != "B":
                            # If we find a pawn, capture it and stop in this direction
                            if board[current_row][current_col] == "p":
                                captured_pawns += 1
                                break
                          
                            # Move to the next cell in the same direction
                            current_row += dx
                            current_col += dy
                  
                    return captured_pawns
        
# @lc code=end

