#!/usr/bin/python


def comb(a, i, v, k):
    if len(v) == k:
        print v
        return
    # inefficient
    # for j in xrange(i, len(a)):
    for j in xrange(i, len(a) - k + len(v) + 1):
        v.append(a[j])
        comb(a, j + 1, v, k)
        v.pop()


a = [1,2,3,4,5]
k = 3
comb(a, 0, [], k)

