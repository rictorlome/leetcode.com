class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        swap = [[False for j in range(len(board[i]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                live = board[i][j] == 1
                num_living_neighbors = self.numLivingNeighbors(board, i, j)
                if live and (3 < num_living_neighbors or num_living_neighbors < 2):
                    swap[i][j] = True
                if not live and num_living_neighbors == 3:
                    swap[i][j] = True

        for i in range(len(board)):
            for j in range(len(board[i])):
                if swap[i][j]:
                    board[i][j] ^= 1
        
    def numLivingNeighbors(self, board, i, j):
        neighbors = self.getNeighbors(board, i, j)
        return len(
            [neighbor for neighbor in neighbors if neighbor == 1]
        )

    def getNeighbors(self, board, i, j):
        min_k, min_l = max(0, i - 1), max(0, j - 1)
        max_k = min(len(board), i + 2)
        max_l =  min(len(board[i]), j + 2)
        return [
            board[k][l] for k in range(min_k, max_k)
            for l in range(min_l, max_l) if not (k == i and l == j)
        ]
        