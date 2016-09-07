#!/usr/bin/python


class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        sieve = [True if i % 2 != 0 else False for i in xrange(n)]
        sieve[0], sieve[1], sieve[2] = False, False, True
        for x in xrange(3, int(n**0.5) + 1):
            if x % 2 != 0 and sieve[x] == True:
                y = x*x
                while y <= n - 1:
                    sieve[y] = False
                    y += x
        return sieve.count(True)


s = Solution()
assert s.countPrimes(0) == 0
assert s.countPrimes(1) == 0
assert s.countPrimes(2) == 0
assert s.countPrimes(3) == 1
assert s.countPrimes(10**6) == 78498
