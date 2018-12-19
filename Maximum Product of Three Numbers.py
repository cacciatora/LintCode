class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    def maximumProduct(self, nums):
        nums = sorted(nums)
        # 0 posivive number
        if nums[-1] <= 0:
            return nums[-1] * nums[-2] * nums[-3]
        # 1 positive number
        if nums[-1] > 0 and nums[-2] <= 0:
            return nums[0] * nums[1] * nums[-1]
        # 2 positive numbers
        if nums[-2] > 0 and nums[-3] <= 0:
            return nums[0] * nums[1] * nums[-2]
        # 3 positive numbers
        if nums[-3] > 0:
            if nums[2] < 0:
                return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
            if nums[2] >= 0:
                return nums[-3] * nums[-2] * nums[-1]