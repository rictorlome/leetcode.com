class Solution:
    def climbStairs(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            if n in memo:
                return memo[n]
            total = 0
            for i in range(1,3):
                total += self.climbStairs(n-i, memo)
            memo[n] = total
            return total

s = Solution()
print(s.climbStairs(35))
