class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        non_zero_idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[non_zero_idx] = nums[i]
            non_zero_idx += 1
        zero_start_idx = non_zero_idx
        nums[zero_start_idx:] = [0] * (len(nums) - zero_start_idx)