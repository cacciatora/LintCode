class Solution:
    """
    @param: nums: an array of integers
    example:[3,12,43,5,2,2]
    @return: nothing
    """

    def partitionArray(self, nums):
        # write your code here
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 1:
                left += 1
                continue
            if nums[right] % 2 == 0:
                right -= 1
                continue
            nums[right], nums[left] = nums[left], nums[right]