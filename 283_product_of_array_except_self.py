class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right, output = [1 for x in nums], [1 for x in nums], [1 for x in nums]

        prod = 1
        for i, el in enumerate(nums[:len(nums)-1]):
            prod *= el
            left[i+1] = prod

        prod = 1
        for i in range(len(nums)-1,-1,-1):
            el = nums[i]
            prod *= el
            if i > 0: right[i-1] = prod

        for i in range(len(nums)):
            output[i] = left[i] * right[i]
        return output

s = Solution()
nums = [1,2,3,4]
