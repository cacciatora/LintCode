class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        left = 0
        right = len(A) - 1
        while left <= right:
            if A[left] == elem:
                del A[left]
                right -= 1
            else:
                left += 1
        return right+1