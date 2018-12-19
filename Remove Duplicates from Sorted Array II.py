class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    exampleï¼[-10,-10,-10,-10,-10,-9,-9,-9,-9,0,2,2,2,2]
    """

    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        indexToPlace = 0
        count = 0
        lastNum = None

        for num in nums:
            if num != lastNum or lastNum == None:
                count = 0
            if count < 2:
                nums[indexToPlace] = num
                indexToPlace += 1
                lastNum = num
                count += 1
        nums = nums[:indexToPlace]
        return indexToPlace