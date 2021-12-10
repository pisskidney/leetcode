"""
70. Climbing Stairs

https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    visited = {}

    def climbStairs(self, n: int) -> int:
        if n in self.visited:
            return self.visited[n]
        if n <= 1:
            return 1
        self.visited[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.visited[n]


def main():
    s = Solution()
    print(s.climbStairs(45))


if __name__ == '__main__':
    raise(SystemExit(main()))
