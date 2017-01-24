#!/usr/bin/python
from random import randint


class RSelect(object):
    def partition(self, A, fr, to, i):
        if to == fr:
            return to + 1
        A[fr], A[i] = A[i], A[fr] 
        k = fr
        for j in xrange(fr + 1, to + 1):
            if A[j] <= A[fr]:
                k += 1
                A[k], A[j] = A[j], A[k]
        A[fr], A[k] = A[k], A[fr]
        return k + 1
    
    def select(self, A, fr, to, i):
        p = randint(fr, to)
        j = self.partition(A, fr, to, p)
        print p, i, j, fr, to, A
        if j == i:
            return A[j-1]
        elif j < i:
            return self.select(A, j, to, i)
        else:
            return self.select(A, fr, j - 2, i)





rs = RSelect()
a = [72,60,9,8,5,4,1]
print a
print 'p i j from to'
print rs.select(a, 0, len(a) - 1, 3)

