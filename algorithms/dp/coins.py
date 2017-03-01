#!/usr/bin/python


'''
Create sum x using as few coins as possible from a.
'''


inf = 2**64


def coins(x, a):
    global inf
    dp = [inf for _ in xrange(x + 1)]
    dp[0] = 0
    for i in xrange(1, x+1):
        smallest = inf
        for j in xrange(len(a)):
            if i - a[j] >= 0:
                smallest = min(smallest, 1 +  dp[i-a[j]])
        dp[i] = smallest
    return dp[-1]


def coins_recursive(x, a):
    if x == 0:
        return 0
    if x < 0:
        global inf
        return inf
    return 1 + min([coins_recursive(x - a[j], a) for j in xrange(len(a))])


a = [1, 3, 4]
summ = 10
print coins_recursive(10, a)
