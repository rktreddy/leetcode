#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # The recursive function to reveal the board starting from the clicked cell.
        def reveal(i: int, j: int):
            # Count mines around the current cell
            mine_count = 0
            for x in range(max(i - 1, 0), min(i + 2, rows)):  # Limits the range on the board
                for y in range(max(j - 1, 0), min(j + 2, columns)):  # Limits the range on the board
                    if board[x][y] == "M":
                        mine_count += 1
          
            # If there are mines around the cell, update with mine count
            if mine_count > 0:
                board[i][j] = str(mine_count)
            else:
                # Otherwise, set the cell to "B" for blank and reveal surrounding cells
                board[i][j] = "B"
                for x in range(max(i - 1, 0), min(i + 2, rows)):
                    for y in range(max(j - 1, 0), min(j + 2, columns)):
                        if board[x][y] == "E":
                            reveal(x, y)

        # Get the size of the board
        rows, columns = len(board), len(board[0])
      
        # The clicked position
        click_row, click_col = click
      
        # If the clicked cell contains a mine, game over
        if board[click_row][click_col] == "M":
            board[click_row][click_col] = "X"
        else:
            # Start revealing from the clicked cell
            reveal(click_row, click_col)
      
        # Return the updated board
        return board
        
# @lc code=end

