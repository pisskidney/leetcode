#!/usr/bin/python


def perm(a, n, b):
    if len(b) == n:
        print b
        return
    for i in xrange(len(a)):
        new = b[:]
        new.append(a[i])
        perm(a[:i] + a[i+1:], n, new)


def perm2(a, p, v):
    if len(v) == len(a):
        print v
        return
    for i in xrange(len(p)):
        if p[i]: continue
        p[i] = 1
        v.append(a[i])
        perm2(a, p, v)
        p[i] = 0
        v.pop()


a = [1, 2, 3]
perm(a, len(a), [])
print '-' * 20
perm2(a, [0 for _ in xrange(len(a))], [])


