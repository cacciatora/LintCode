class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        newArray=[0] * (len(A) + len(B))
        indexOfA=indexOfB = 0
        while indexOfA <len(A) and indexOfB <len(B):
            if A[indexOfA] < B[indexOfB]:
                newArray[indexOfA+indexOfB]=A[indexOfA]
                indexOfA+=1
            else:
                newArray[indexOfA+indexOfB]=B[indexOfB]
                indexOfB+=1
        if indexOfA<len(A):
            newArray[indexOfA+indexOfB:]=A[indexOfA:]
        elif indexOfB<len(B):
            newArray[indexOfA+indexOfB:]=B[indexOfB:]
        return newArray