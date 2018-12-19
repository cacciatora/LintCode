class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """

    def findMaxAverage(self, nums, k):
        if len(nums) == 1:
            return nums[0] * 1.0

        maximum_ave = max(round(sum(nums[0:k]) / float(k), 2), round(sum(nums[len(nums) - k:]) / float(k), 2))
        print(maximum_ave)
        current_ave = 0
        for i in range(k, len(nums)):
            if nums[i] > nums[i - k]:
                continue
            current_ave = round(sum(nums[i - k:i]) / float(k), 2)
            print(current_ave)
            if maximum_ave < current_ave:
                maximum_ave = current_ave
        return maximum_ave