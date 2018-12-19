class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        maxsum_left_to_right = []
        maxsum_right_to_left = []

        maxsum_left_to_right.append(nums[0])
        previous_sum = nums[0]

        for i in range(1, len(nums)):
            if previous_sum + nums[i] > nums[i]:
                previous_sum += nums[i]
            else:
                previous_sum = nums[i]
            if maxsum_left_to_right[-1] > previous_sum:
                maxsum_left_to_right.append(maxsum_left_to_right[-1])
            else:
                maxsum_left_to_right.append(previous_sum)

        maxsum_right_to_left.append(nums[-1])
        post_sum = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if post_sum + nums[i] > nums[i]:
                post_sum += nums[i]
            else:
                post_sum = nums[i]
            if maxsum_right_to_left[-1] > post_sum:
                maxsum_right_to_left.append(maxsum_right_to_left[-1])
            else:
                maxsum_right_to_left.append(post_sum)
        print(maxsum_left_to_right)
        print(maxsum_right_to_left)
        maxsum_right_to_left.reverse()

        max_sum = maxsum_left_to_right[0] + maxsum_right_to_left[1]

        for i in range(1, len(maxsum_left_to_right) - 1):
            tmp = maxsum_left_to_right[i] + maxsum_right_to_left[i + 1]
            if max_sum < tmp:
                max_sum = tmp
        return max_sum