"""
91. Decode Ways

https://leetcode.com/problems/decode-ways/
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0
        dp = [0 for _ in s]
        valid = set([str(x) for x in range(1, 27)])
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] in valid:
                dp[i] += dp[i-1]
            if s[i-1:i+1] in valid:
                if i - 2 < 0:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[-1]


def main():
    s = Solution()
    print(s.numDecodings('226'))
    print(s.numDecodings('0'))
    print(s.numDecodings('00000'))
    print(s.numDecodings('000003'))
    print(s.numDecodings(''))


if __name__ == '__main__':
    raise(SystemExit(main()))
