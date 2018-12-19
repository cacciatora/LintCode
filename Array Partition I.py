class Solution:
    """
    @param nums: an array
    @return: the sum of min(ai, bi) for all i from 1 to n
    """
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        res = 0
        for i in range(len(nums)/2):
            res += nums[i*2]
        return res