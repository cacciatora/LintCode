class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """

    def rotate(self, nums, k):
        # Write your code here
        k = k % len(nums)
        left = 0
        p = len(nums) - k - 1
        while left < p:
            nums[left], nums[p] = nums[p], nums[left]
            left += 1
            p -= 1

        right = len(nums) - 1
        p = len(nums) - k
        while p < right:
            nums[p], nums[right] = nums[right], nums[p]
            p += 1
            right -= 1
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums