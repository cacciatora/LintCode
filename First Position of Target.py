class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        if target < nums[0] or target > nums[-1]:
            return -1

        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[(left + right) / 2] >= target:
                right = (left + right) / 2
            elif nums[(left + right) / 2] < target:
                left = (left + right) / 2 + 1
        if nums[left] == target:
            return left
        else:
            return -1