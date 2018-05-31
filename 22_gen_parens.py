class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1: return ['()']
        prev = self.generateParenthesis(n-1)
        return sorted(list({
         s[:i] + '({})'.format(s[i:]) for s in prev for i in range(len(s)+1)
        }))
