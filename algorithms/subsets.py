#!/usr/bin/python


x = [1, 3, 7, 2, 4, 5]
c = 0


def subsets(n, a, acc):
    if n == len(x):
        acc.append(a[:])
        return 
    subsets(n+1, a, acc)
    a.append(x[n-1])
    subsets(n+1, a, acc)
    a.pop()


def subsets_iterative(a, acc):
    from collections import deque
    queue = deque([a[:]])
    while queue:
        subset = queue.popleft()
        if subset not in acc:
            acc.append(subset)
        for i in xrange(len(subset)):
            queue.append(subset[:i] + subset[i + 1:])
    return acc


def subsets_iterative2(a, acc):
    n = len(a)
    for bitmask in xrange(2**n):
        subset = []
        for j in xrange(n):
            if (1 << j) & bitmask:
                subset.append(a[j])
        acc.append(subset)
    return acc


subs = []
subsets_iterative2(x, subs)
print subs, len(subs)
