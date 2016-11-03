#!/usr/bin/python


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0, 1, 1, 2] + [0] * num
        i = 4
        half = 6
        cut = 8
        lookback = 2
        while i <= num:
            if i >= cut:
                half *= 2
                cut *= 2
                lookback *= 2
            if i < half:
                dp[i] = dp[i-lookback]
            else:
                dp[i] = dp[i-lookback] + 1
            i += 1
        return dp[:num+1]


s = Solution()
print s.countBits(35)
