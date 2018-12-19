class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        # write your code here
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            for i in range(len(digits) - 1, -1, -1):
                if i == 0 and digits[0] == 9:
                    return [1] + [0] * len(digits)

                if digits[i] != 9:
                    digits[i] += 1
                    return digits
                else:
                    digits[i] = 0