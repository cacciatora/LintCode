class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        if len(nums) > 0:
            maxSum = nums[0]
            previousSum = nums[0]
            # maxSumSubArray=[]
            # currentArray=[nums[0]]

            for i in range(1, len(nums)):
                if previousSum + nums[i] > nums[i]:
                    # currentArray.append(nums[i])
                    previousSum += nums[i]
                elif previousSum + nums[i] <= nums[i]:
                    # currentArray=[nums[i]]
                    previousSum = nums[i]
                if previousSum > maxSum:
                    # maxSumSubArray=list(currentArray)
                    maxSum = previousSum
        return maxSum