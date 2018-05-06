import sys

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        sorted_coins = sorted(coins)
        memo_table = [[ 0 if total is 0 else sys.maxsize for total in range(amount+1)] for coin in coins]
        for i,row in enumerate(memo_table):
            coin_val = sorted_coins[i]
            for j,col in enumerate(memo_table[i]):
                if i is 0:
                    memo_table[i][j] = j//coin_val if j % coin_val is 0 else sys.maxsize
                else:
                    memo_table[i][j] = min(
                        1 + memo_table[i][j-coin_val] if j >= coin_val else sys.maxsize,
                        memo_table[i-1][j]
                    )
        res = memo_table[len(coins)-1][amount]
        return (res is sys.maxsize ? -1 : res)
