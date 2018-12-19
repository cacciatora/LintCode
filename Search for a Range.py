class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        sorted(A)
        if len(A) == 0:
            return [-1, -1]
        if len(A) == 1:
            if A[0] != target:
                return [-1, -1]
            else:
                return [0, 0]

        result = []
        left = 0
        right = len(A) - 1

        while left <= right:

            if A[left] > target:
                return [-1, -1]
            if A[left] == target:
                result.append(left)
                break

            mid = (left + right) / 2
            if A[mid] < target:
                left = mid + 1

            elif A[mid] >= target:
                right = mid
            # if left == right:
            #    return [-1,-1]
        print(result)

        left = 0
        right = len(A) - 1
        while left <= right:

            if A[right] < target:
                return [-1, -1]
            if A[right] == target:
                result.append(right)
                break

            mid = (left + right) / 2
            if A[mid] <= target:
                left = mid
            elif A[mid] > target:
                right = mid - 1

            # if left == right:
            #    result.append(left)

        return result