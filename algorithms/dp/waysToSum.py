#!/usr/bin/python

'''
Given a target sum T, how many ways to sum to T using coins in A.
'''


def ways(target, coins):
    dp = [-1 for _ in xrange(target+1)]
    dp[0] = 1
    for i in xrange(1, target + 1):
        nr_ways = 0
        for j in xrange(len(coins)):
            if i - coins[j] >= 0:
                nr_ways += dp[i-coins[j]]
        dp[i] = nr_ways
    return dp[-1]


def ways_recursive(target, coins):
    if target < 0:
        return 0
    if target == 0:
        return 1
    return sum([ways_recursive(target - coins[j], coins) for j in xrange(len(coins))])


target = 5
coins = [1, 3, 4]
print ways(target, coins)
print ways_recursive(target, coins)
