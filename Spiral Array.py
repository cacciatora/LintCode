import copy
class Solution:
    """
    @param n: a Integer
    @return: a spiral array
    """

    def spiralArray(self, n):
        # write your code here
        spiral = [[0 for col in range(n)] for row in range(n)]
        spiral[0] = range(1,n+1)
        if n % 2 :
            i, j = (n-1)/2, (n-1)/2
            current = n * n
            spiral[i][j] = current
            print(spiral)
            for moves in range(1,n):
                if moves % 2 :
                    for move in range(1,moves+1):
                        j -= 1
                        current -= 1
                        spiral[i][j] = current
                    for move in range(1,moves+1):
                        i += 1
                        current -= 1
                        spiral[i][j] =current
                else:
                    for move in range(1, moves+1):
                        j += 1
                        current -= 1
                        spiral[i][j] = current
                    for move in range(1,moves+1):
                        i -= 1
                        current -= 1
                        spiral[i][j] = current
        elif not n % 2 :
            i, j = n/2 , n/2 - 1
            current = n * n
            spiral[i][j] = current
            for moves in range(1,n):
                if moves % 2 :
                    for move in range(1,moves+1):
                        j += 1
                        current -= 1
                        spiral[i][j] = current
                    for move in range(1,moves+1):
                        i -= 1
                        current -= 1
                        spiral[i][j] = current
                else:
                    for move in range(1,moves+1):
                        j -= 1
                        current -= 1
                        spiral[i][j] = current
                    for move in range(1,moves+1):
                        i += 1
                        current -= 1
                        spiral[i][j] = current
        return spiral