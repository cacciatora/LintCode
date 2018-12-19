class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            target = 0 - nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if start > i + 1 and nums[start] == nums[start - 1]:
                    start += 1
                    continue
                cur_sum = nums[start] + nums[end]
                if cur_sum == target:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                elif cur_sum < target:
                    start += 1
                else:
                    end -= 1
        return ans