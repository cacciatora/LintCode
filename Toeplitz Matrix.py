class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """

    def isToeplitzMatrix(self, matrix):
        if len(matrix) <= 1 or len(matrix[0]) <= 1:
            return True

        m, n = len(matrix), len(matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True