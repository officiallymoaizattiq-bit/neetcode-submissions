class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen=set()
            for val in range(9):
                if board[row][val] != ".":
                    if (board[row][val]) in seen:
                        return False
                    else:
                        seen.add(board[row][val])
        for col in range(9):
            seen=set()
            for val in range(9):
                if board[val][col] != ".":
                    if (board[val][col]) in seen:
                        return False
                    else:
                        seen.add(board[val][col])
        startCol=0
        startRow=0
        for startRow in range(0,9,3):
            for startCol in range(0,9,3):
                seen=set()
                for row in range(startRow,startRow+3):
                    for col in range(startCol,startCol+3):
                        if board[row][col] != ".":
                            if (board[row][col]) in seen:
                                return False
                            else:
                                seen.add(board[row][col])

        return True           
                