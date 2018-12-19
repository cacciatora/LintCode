class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        if len(A) == 0:
            return -1
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2

            if A[mid] == target:
                return mid
            elif A[mid] > A[right]:
                if A[left] <= target and A[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1