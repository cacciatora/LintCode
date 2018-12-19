class Solution:
    """
    @param bits: a array represented by several bits.
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        if len(bits) == 1:
            return True
        start = len(bits) - 2
        count_1 = 0
        while start >= 0:
            if bits[start] != 0:
                count_1 += 1
            else:
                break
            start -= 1
        if count_1 % 2  :
            return False
        else:
            return True