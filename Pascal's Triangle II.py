class Solution:
    """
    @param rowIndex: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """
    def getRow(self, rowIndex):
        # write your code here
        def c(n,k):
            if k == 0 or k == n:
                return 1
            return reduce(lambda x,y:x * y, range(n - k + 1,n+1)) / reduce(lambda x,y:x * y, range(1,k + 1))
        res = [1 for _ in range(rowIndex + 1)]
        for i in range((rowIndex + 2) / 2):
            res[i] = res[-(i+1)] = c(rowIndex,i)
        return res