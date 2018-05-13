/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */

 var exist = function(board, word) {
   for (let i = 0; i < board.length; i++) {
     for (let j = 0; j < board[i].length; j++) {
       let letter = board[i][j];
       if (letter === word[0] && dfs(i,j,word.slice(1),{},board)) {
         return true;
       }
     }
   }
   return false;
 }

 function neighbors(board, i, j) {
   const res = [];
   const possibles = [
     [i + 1, j],
     [i - 1, j],
     [i, j + 1],
     [i, j - 1]
   ]
   for (let k = 0; k < possibles.length; k++) {
     let x = possibles[k][0];
     let y = possibles[k][1];
     if (isOnBoard(board,x,y)) {
       res.push([x,y])
     }
   }
   return res;
 }

 function isOnBoard(board, i, j) {
   return 0 <= i && i < board.length && 0 <= j && j < board[i].length;
 }

 function dfs(i, j, word, seen, board) {
   if (word.length === 0) return true;
   seen[[i,j]] = true
   const nbs = neighbors(board, i, j);
   for (let q = 0; q < nbs.length; q++) {
     let [n, m] = nbs[q];
     let nextLetter = word[0]
     if (board[n][m] === nextLetter && !seen[[n,m]] && dfs(n, m, word.slice(1), seen, board)) {
       return true;
     }
   }
   seen[[i,j]] = false;
   return false;
 }

let m = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
let w = "ABCCED"
console.log(exist(m,w))
