class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if len(A) < 2:
            return len(A)

        res = 2
        count = 2
        for i in range(2, len(A)):
            if (A[i - 1] - A[i - 2]) * (A[i] - A[i - 1]) > 0:
                count += 1
            else:
                count = 2
            if res < count:
                res = count
        return res