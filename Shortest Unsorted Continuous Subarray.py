class Solution:
    """
    @param nums: an array
    @return: the shortest subarray's length
    """
    def findUnsortedSubarray(self, nums):
        # Write your code here
        sorted_nums = sorted(nums);
        i,j = 0,len(nums)-1
        while i <= j:
            if nums[i] == sorted_nums[i]:
                i += 1
                continue
            if nums[j] == sorted_nums[j]:
                j -= 1
                continue
            break
        return j - i + 1