#!/usr/bin/python

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def findRightInterval(self, intervals):
        indexes = sorted(range(len(intervals)), key=lambda i: intervals[i].start)
        intervals = sorted(intervals, key=lambda i: i.start)
        res = [-1 for _ in xrange(len(intervals))]
        for i in xrange(len(intervals) - 1):
            left = i + 1
            right = len(intervals) - 1
            current = None
            while left <= right:
                mid = (left + right) / 2
                if intervals[mid].start >= intervals[i].end:
                    current = indexes[mid]
                    right = mid - 1
                else:
                    left = mid + 1
            if current is not None:
                res[indexes[i]] = current
        return res


class SolutionNaiveQuadratic(object):
    def findRightInterval(self, intervals):
        res = [-1 for _ in intervals]
        for i in xrange(len(intervals)-1):
            for j in xrange(i+1, len(intervals)):
                a, b = intervals[i], intervals[j]
                if a.end <= b.start:
                    if res[i] == -1:
                        res[i] = j
                    elif intervals[res[i]].start - a.end > b.start - a.end:
                        res[i] = j
                if b.end <= a.start:
                    if res[j] == -1:
                        res[j] = i
                    elif intervals[res[j]].start - b.end > a.start - b.end:
                        res[j] = i
        return res


s = Solution()
a = [ [1,4], [2,3], [3,4] ]
a = [[3,4],[2,3],[1,2]]
b = []
for x in a:
    b.append(Interval(s=x[0], e=x[1]))
print s.findRightInterval(b)
