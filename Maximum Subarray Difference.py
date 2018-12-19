class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """

    def maxDiffSubArrays(self, nums):

        n = len(nums)
        max_left = [0] * n
        min_left = [0] * n
        max_local_sum = nums[0]
        min_local_sum = nums[0]
        max_global_sum = nums[0]
        min_global_sum = nums[0]

        # init
        max_left[0] = max_global_sum
        min_left[0] = min_global_sum

        for i in range(1, len(nums)):
            max_local_sum = max(max_local_sum + nums[i], nums[i])
            max_global_sum = max(max_local_sum, max_global_sum)
            max_left[i] = max_global_sum

            min_local_sum = min(min_local_sum + nums[i], nums[i])
            min_global_sum = min(min_local_sum, min_global_sum)
            min_left[i] = min_global_sum

        max_right = [0] * n
        min_right = [0] * n
        max_local_sum = nums[-1]
        min_local_sum = nums[-1]
        max_global_sum = nums[-1]
        min_global_sum = nums[-1]

        # init
        max_right[-1] = max_global_sum
        min_right[-1] = min_global_sum

        for i in range(len(nums) - 2, -1, -1):
            max_local_sum = max(max_local_sum + nums[i], nums[i])
            max_global_sum = max(max_local_sum, max_global_sum)
            max_right[i] = max_global_sum

            min_local_sum = min(min_local_sum + nums[i], nums[i])
            min_global_sum = min(min_local_sum, min_global_sum)
            min_right[i] = min_global_sum

        print(max_left)
        print(min_left)
        print(max_right)
        print(min_right)
        result = max(abs(max_left[0] - min_right[1]), abs(min_left[0] - max_right[1]))

        for i in range(1, len(nums) - 1):
            result = max(result, abs(max_left[i] - min_right[i + 1]), abs(min_left[i] - max_right[i + 1]))

        return result