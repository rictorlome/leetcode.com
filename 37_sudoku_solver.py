## Help from https://www.youtube.com/watch?v=NuodN41aK3g
## Note - this returns True/False instead of void per rtype specified below

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        i,j = self.first_empty(board)
        if i == -1: return True

        possibles = self.possibilities(board,i,j)
        for pos in possibles:
            board[i][j] = pos
            if self.solveSudoku(board): return True
        board[i][j] = '.'
        return False

    def first_empty(self,board):
        for i,row in enumerate(board):
            for j,sq in enumerate(row):
                if sq == '.': return i,j
        return -1,-1

    def possibilities(self,board,i,j):
        row = set([board[i][x] for x in range(9)])
        col = set([board[x][j] for x in range(9)])
        sq = set(self.get_square(board,(i//3)*3,(j//3)*3))
        u = row.union(col,sq)
        return [str(p) for p in range(1,10) if str(p) not in u]

    def get_square(self,board,i,j):
        return [board[row][col] for row in range(i,i+3) for col in range(j,j+3)]


s = Solution()
b1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(
s.solveSudoku(b1),
b1
)
