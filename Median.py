class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def patition(self, array, left, right):
        pivot = array[right]
        i = left
        for j in range(left, right):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[right] = array[right], array[i]
        return left, i, right

    def median(self, nums):
        mdianIndex = (len(nums) + 1) / 2 - 1
        left, currentIndex, right = self.patition(nums, 0, len(nums) - 1)
        # print(nums)
        # print(currentIndex)

        while currentIndex != mdianIndex:
            if currentIndex > mdianIndex:
                left, currentIndex, right = self.patition(nums, left, currentIndex - 1)
            if currentIndex < mdianIndex:
                left, currentIndex, right = self.patition(nums, currentIndex + 1, right)
            # print(nums)
        return nums[currentIndex]