#!/usr/bin/python
'''
Given a positive integer X, replace to consecutive digits with the largest one
s.t. the number is as small as possible:
233614 becomes 23364, since we replace 1 and 4 with 4.
'''


from math import log


def solve(x):
    minn = x
    l = int(log(x, 10))
    n = x % 10 ** l
    last = x / 10 ** l
    for i in xrange(l - 1, -1 ,-1):
        cur = n % 10 ** i
        left = (x / 10 ** (i+2)) * 10 ** (i + 1)
        this = max(last, cur) * 10 ** i
        right = x % 10 ** i
        minn = min(minn, left + this + right)
        last = cur
        n %= 10 ** i
    return minn
    

print solve(233614)
print solve(123456)
print solve(329999)
