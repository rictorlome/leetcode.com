class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """Works for 32 bit ints"""
        rev = 0
        for i in range(32):
            if n & (1 << i):
                rev |= (1 << (31 - i))
        return rev
