class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        axis = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                axis = i
                break
        if axis != -1:

            left = 0
            right = axis
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1

            left = axis + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1

            left = 0
            right = len(nums) - 1
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1