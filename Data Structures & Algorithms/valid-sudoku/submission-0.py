from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        t = True
        for i in range(9):
            for j in range(9):
                if board[i].count(board[i][j]) >1 and board[i][j] != ".":
                    return False
        for j in range(9):
            col = []
            for i in range(9):
                if board[i][j] != ".":
                    col.append(board[i][j])
            if len(col)!=len(set(col)):
                    return False
                    
        for i in range(0,9,3):
            for j in range(0,9,3):
                subbox = [row[i:i+3] for row in board[j:j+3]]
                flat = [n for row in subbox for n in row if n!="."]
                if len(flat) != len(set(flat)):
                    return False
        return True

