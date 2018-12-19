class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        if len(nums) > 0:
            previousSum = nums[0]
            minSum = previousSum

            for i in range(1, len(nums)):
                if previousSum + nums[i] < nums[i]:
                    previousSum += nums[i]
                else:
                    previousSum = nums[i]
                if minSum > previousSum:
                    minSum = previousSum
            return minSum