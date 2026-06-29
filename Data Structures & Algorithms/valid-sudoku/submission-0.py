class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                else:
                    seen.add(cell)        
            for col in range(9):
                seen = set()
                for row in range(9):
                    cell = board[row][col]
                    if cell == ".":
                        continue
                    if cell in seen:
                        return False
                    else:
                        seen.add(cell)
            for box_row in range(0,9,3):
                for box_col in range(0,9,3):
                    seen = set()
                    for r in range(3):
                        for c in range(3):
                            cell = board[box_row + r][box_col + c]
                            if cell == ".":
                                continue
                            if cell in seen:
                                return False
                            else:
                                seen.add(cell)        
        return True
