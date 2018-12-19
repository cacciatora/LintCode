"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        result = list1 + list2
        result = sorted(result,key = lambda x: x.start)
        point = 1
        end = len(result)
        while point < end :
            if result[point-1].end < result[point].start:
                point += 1
                continue
            result[point-1].end = max(result[point-1].end, result[point].end)
            result.pop(point)
            end -= 1
        return result