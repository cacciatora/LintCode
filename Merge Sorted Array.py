class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        insertIndex, ia, ib = m + n - 1, m - 1, n - 1

        while ia >= 0 or ib >= 0:
            if ib < 0:
                break

            elif ia >= 0 and A[ia] > B[ib]:
                A[insertIndex] = A[ia]
                ia -= 1

            elif ia >= 0 and A[ia] <= B[ib]:
                A[insertIndex] = B[ib]
                ib -= 1

            elif ia < 0:
                A[:ib + 1] = B[:ib + 1]
                break
            insertIndex -= 1