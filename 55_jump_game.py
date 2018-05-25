class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        zero_idxes = set()
        for i, el in enumerate(nums):
            if el == 0 and i != len(nums)-1:
                zero_idxes.add(i)

        return all([self.num_past_idx(nums,idx) for idx in zero_idxes])

    def num_past_idx(self,nums,idx):
        return any([i+el > idx for i, el in enumerate(nums[:idx])])
