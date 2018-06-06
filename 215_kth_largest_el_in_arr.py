class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        part_idx = self.partition(nums)
        target_idx = len(nums) - k
        if part_idx == target_idx:
            return nums[part_idx]
        elif part_idx < target_idx:
            return self.findKthLargest(nums[part_idx+1:],k)
        else:
            return self.findKthLargest(nums[:part_idx],k-(len(nums)-part_idx))

    def partition(self,nums):
        low, high, pivot = 0, len(nums)-2, nums[len(nums)-1]
        while low <= high:
            while low <= high and nums[low] < pivot:
                low += 1
            while low <= high and pivot <= nums[high]:
                high -= 1
            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
        nums[low],nums[len(nums)-1] = nums[len(nums)-1],nums[low]
        return low

s = Solution()
nums = [1,2,3,4,5,6]
for i, el in enumerate(nums):
    print(s.findKthLargest(nums,el) == nums[len(nums)-(i+1)])
