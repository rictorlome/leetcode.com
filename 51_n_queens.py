class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        pos_dict = {}
        placed = self.place_queen_on_row(0,n,pos_dict)
        return pos_dict.values() if placed else []


    def place_queen_on_row(self,row,n,pos_dict):
        if row is n: return True

        for col in range(n):
            possiblity = [row,col]
            conflict = any([self.is_conflict(pos,row,col) for dpth, pos in pos_dict.items()])
            if not conflict:
                pos_dict[row] = possiblity
                nxt = self.place_queen_on_row(row+1,n,pos_dict)
                if nxt:
                    return True
                else:
                    del pos_dict[row]
        return False


    def is_conflict(self,pos,row,col):
        r, c = pos
        return row is r or col is c or row+col is r+c or row-col is r-c
