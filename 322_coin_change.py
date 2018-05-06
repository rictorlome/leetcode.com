import sys

class Solution:
    def big_table_coin_change(self, coins, amount):
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
        return -1 if res is sys.maxsize else res


    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #Note: replace sys.maxsize with BIGNUM on leetcode to prevent timeouts.
        #BIGNUM = 1000000
        total_arr = [0 if amt is 0 else sys.maxsize for amt in range(amount+1)]
        which_coin = [-1 for _ in range(amount+1)]

        for j, denom in enumerate(coins):
            for i, amt in enumerate(total_arr):
                if denom > i or denom > amount: continue
                if total_arr[i] > 1 + total_arr[i - denom]:
                    which_coin[i] = j
                    total_arr[i] = 1 + total_arr[i - denom]
        return total_arr[amount] if total_arr[amount] is not sys.maxsize else -1


## Example
s = Solution()
c = [7,2,3,6]
amt = 13
print(s.coinChange(c,amt))
