class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        fallen = ""
        for idx, domino in enumerate(dominoes):
            fall = domino
            if domino == ".":
                lpush_d = self.l_push_distance(idx, dominoes)
                rpush_d = self.r_push_distance(idx, dominoes)
                if lpush_d < rpush_d:
                    fall = "R"
                elif rpush_d < lpush_d:
                    fall = "L"
                else:
                    fall = "."
            fallen += fall
        return fallen

    def l_push_distance(self, idx, dominoes):
        for i in range(idx-1, -1, -1):
            if dominoes[i] == "L":
                break
            if dominoes[i] == "R":
                return idx - i
        return float("inf")

    def r_push_distance(self, idx, dominoes):
        for i in range(idx+1, len(dominoes)):
            if dominoes[i] == "R":
                break
            if dominoes[i] == "L":
                return i - idx
        return float("inf")

    tests = [
        (".L.R...LR..L..", "LL.RR.LLRRLL.."),
        ("RR.L", "RR.L"),
        ("L.R", "L.R"),
        ("R.L", "R.L"),
        (".L", "LL"),
        (".R", ".R"),
        ("R.", "RR")
    ]

    def test(self):
        for t in Solution.tests:
            if not self.pushDominoes(t[0]) == t[1]:
                print('Wrong answer for {} -- Got {}, Expected {}'.format(
                    t[0], self.pushDominoes(t[0]), t[1]
                ))
                assert(False)


s = Solution()
s.test()
