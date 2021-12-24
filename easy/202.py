"""
202. Happy Number

https://leetcode.com/problems/happy-number/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([])
        while True:
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            new = 0
            for digit in str(n):
                digit = int(digit)
                new += digit * digit
            n = new

def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
