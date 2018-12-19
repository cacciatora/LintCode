class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        dictOfResult = {}
        for i in range(len(numbers)):
            dictOfResult[target - numbers[i]] = i

        for index1 in range(len(numbers)):
            if dictOfResult.has_key(numbers[index1]):
                index2 = dictOfResult[numbers[index1]]
                if index1 < index2:
                    return [index1, index2]
                else:
                    return [index2, index1]