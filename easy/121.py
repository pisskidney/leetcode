#!/usr/bin/python


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        res = 0
        dp = [0] * len(prices)
        dp[0] = prices[0]
        for i in xrange(1, len(prices)):
            if prices[i] < dp[i-1]:
                dp[i] = prices[i]
            else:
                dp[i] = dp[i-1]
        for i in xrange(1, len(prices)):
            if prices[i] - dp[i] > res:
                res = prices[i] - dp[i]
        return res

            
s = Solution()
x = [7, 1, 5, 3, 6, 4]
print s.maxProfit(x)
