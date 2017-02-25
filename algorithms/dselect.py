#!/usr/bin/python
from sys import exit


class DSelect(object):
    '''Deterministic i'th order selection algorithm that is guaranteed
    to run in O(n).'''

    def partition(self, A, start, end, pivot):
        A[start], A[pivot] = A[pivot], A[start]
        j = 0
        for i in xrange(start + 1, end + 1):
            if A[i] <= A[0]:
                j += 1
                A[j], A[i] = A[i], A[j]
        A[0], A[j] = A[j], A[0]
        return j

    def choose_pivot(self, A, start, end):
        fromm = start
        C = []
        print A, start, end
        while fromm + 4 <= end:
            A[fromm:fromm+5] = sorted(A[fromm:fromm+5])
            median = A[fromm+2]
            C.append(median)
            fromm += 5
        if fromm <= end:
            A[fromm:end+1] = sorted(A[fromm:end+1])
            C.append(A[(fromm+end)/2])
        print C
        return self.select(C, 0, len(C) - 1, (len(C) - 1) / 2)

    def select(self, A, start, end, k):
        if start > end:
            return
        if start == end:
            return end
        pivot = self.choose_pivot(A, start, end)
        pivot = self.partition(A, start, end, pivot)
        '''
        if pivot == k:
            return A[pivot]
        elif pivot < k:
            return self.select(A, start, pivot - 1, k)
        else:
            return self.select(A, pivot + 1, end, k - pivot)
        '''


import random
ds = DSelect()
A = range(1, 20)
random.shuffle(A)
print ds.select(A, 0, len(A) - 1, 3)


def test_partition(ds):
    a = range(10, 0, -1)
    pivot = ds.partition(a, 0, len(a)-1, 4)
    assert pivot == 5

    a = [1]
    pivot = ds.partition(a, 0, 0, 0)
    assert pivot == 0

    a = [2, 1]
    pivot = ds.partition(a, 0, 1, 0)
    assert pivot == 1
    
    a = [1, 2]
    pivot = ds.partition(a, 0, 1, 0)
    assert pivot == 0
    
    a = [2, 1, 3]
    pivot = ds.partition(a, 0, 2, 0)
    assert pivot == 1

ds = DSelect()
test_partition(ds)
