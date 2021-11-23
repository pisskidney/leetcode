"""
93. Restore IP Addresses

https://leetcode.com/problems/restore-ip-addresses/
"""
from typing import List


class Solution:
    def valid(self, s: str) -> bool:
        if s == '0':
            return True
        if s.startswith('0'):
            return False
        if int(s) > 255:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        dp = [[] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(3):
                if i - j < 0:
                    break
                if not self.valid(s[i-j:i+1]):
                    continue
                if i - j - 1 < 0:
                    dp[i].append([s[i-j:i+1]])
                else:
                    for subset in dp[i-j-1]:
                        if len(subset) <= 3:
                            if len(subset) == 3 and i < len(s) - 1:
                                continue
                            dp[i].append(subset + [s[i-j:i+1]])
        return ['.'.join(x) for x in dp[-1] if len(x) == 4]


def main():
    s = Solution()
    print(s.restoreIpAddresses('101023'))


if __name__ == '__main__':
    raise(SystemExit(main()))
