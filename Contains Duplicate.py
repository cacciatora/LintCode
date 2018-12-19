class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        dict_nums = {}
        for i in range(len(nums)):
            if dict_nums.get(nums[i]) == None:
                dict_nums[nums[i]] = i
            else:
                return True
        return False