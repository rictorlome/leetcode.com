class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if self.bad(row): return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                if self.bad(self.get_square(board,i,j)): return False
                
        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if self.bad(col): return False

        return True

    def get_square(self,board,i,j):
        res = []
        for row in range(i,i+3):
            for col in range(j,j+3):
                res.append(board[row][col])
        return res

    def bad(self,row):
        return self.has_dup(row) or self.bad_val(row)

    def has_dup(self,row):
        nums = [x for x in row if x != '.']
        return len(nums) != len(set(nums))

    def bad_val(self,row):
        return not all([1 <= int(el) <= 9 for el in row if el != '.'])


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
b2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# print(s.get_square(b1,3,3))
print(s.isValidSudoku(b2))
