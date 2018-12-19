"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.

    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals,key = lambda x: x.start)

        result = []

        for idx in range(0,len(intervals)):
            if not result or result[-1].end < intervals[idx].start:
                result.append(intervals[idx])
            else:
                result[-1].end = max(result[-1].end,intervals[idx].end)
        return resul
        """

    def merge(self, intervals):
        # write your code here
        # O(nlogn)æ¶é´å¤æåº¦, O(1) extra space
        i = 1
        l = len(intervals)
        intervals = sorted(intervals, key=lambda x: x.start)
        while i < l and l > 1:
            # print i, l, intervals
            start, end = intervals[i].start, intervals[i].end
            prevStart, prevEnd = intervals[i - 1].start, intervals[i - 1].end
            # print start, end, prevStart, prevEnd
            if prevEnd < start:
                i += 1
                continue
            intervals[i - 1].end = max(prevEnd, end)
            intervals.pop(i)
            l -= 1
        return intervals