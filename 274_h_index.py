class Solution:
    def h_index(self, citations):
        srt_cit = sorted(citations, reverse=True)
        best = 0
        for i, val in enumerate(srt_cit):
            if val > i and i + 1 > best:
                best = i + 1
        return best

    def tests(self):
        for test in [
            ([3, 0, 6, 1, 5], 3),
            ([], 0),
            ([0], 0),
            ([0, 0], 0),
            ([100], 1),
            ([11, 15], 2),
            ([4, 4, 0, 0], 2)
        ]:
            if self.h_index(test[0]) != test[1]:
                print("test failed for {}. got {}, expected {}".format(
                    test[0], self.h_index(test[0]), test[1]
                ))
                assert(False)


s = Solution()
s.tests()
