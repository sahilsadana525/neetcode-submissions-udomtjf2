from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.l = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for i in range(len(self.l)):
            if i >= row1 and i <= row2:
                s = s + sum(self.l[i][col1:col2+1])
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)