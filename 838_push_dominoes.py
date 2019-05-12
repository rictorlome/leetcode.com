class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        r_forces, l_forces = [], []
        max_force = len(dominoes)
        current_force = 0
        for domino in dominoes:
            if domino == "R":
                current_force = max_force
            if domino == "L":
                current_force = 0
            r_forces.append(current_force)
            if current_force > 0:
                current_force -= 1

        current_force = 0
        for domino in dominoes[::-1]:
            if domino == "L":
                current_force = -max_force
            if domino == "R":
                current_force = 0
            l_forces.append(current_force)
            if current_force < 0:
                current_force += 1

        l_forces = l_forces[::-1]
        d = [self.to_letter(r_forces[i] + l_forces[i])
             for i in range(len(dominoes))]
        return "".join(d)

    def to_letter(self, num):
        if num < 0:
            return "L"
        if num > 0:
            return "R"
        return "."

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
