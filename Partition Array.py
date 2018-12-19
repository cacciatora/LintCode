class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here

        if len(nums) <= 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] < k:
                left += 1
                continue
            if nums[right] >= k:
                right -= 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
        for i in range(len(nums)):
            if nums[i] < k:
                continue
            return i
        return len(nums)