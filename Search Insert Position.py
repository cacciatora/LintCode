class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """

    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0
        elif len(A) > 0:
            leftIndex = 0
            rightIndex = len(A) - 1

            if A[leftIndex] >= target:
                return 0

            elif A[rightIndex] < target:
                return rightIndex + 1

            else:
                while leftIndex <= rightIndex:

                    midIndex = (leftIndex + rightIndex) / 2

                    if A[midIndex] == target:
                        return midIndex
                    elif A[midIndex] < target:
                        leftIndex = midIndex + 1
                    else:
                        rightIndex = midIndex - 1

                    if A[leftIndex] >= target:
                        return leftIndex
                    elif A[rightIndex] < target:
                        return rightIndex + 1