class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """
    def containsNearbyDuplicate(self, nums, k):
        # Write your code here
        dict_nums = {}
        for i in range(len(nums)):
            if dict_nums.get(nums[i]) == None:
                dict_nums[nums[i]] = i
            else:
                maxium_dis = i - dict_nums[nums[i]]
                if maxium_dis <= k:
                    return True
                else:
                    dict_nums[nums[i]] = i
        return False