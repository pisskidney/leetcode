"""
97. Interleaving String

https://leetcode.com/problems/interleaving-string/
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def go(p1, p2, p3):
            if (key := (p1, p2, p3)) in memo:
                return memo[key]
            if p3 >= len(s3):
                return True
            if p1 >= len(s1):
                if s2[p2] == s3[p3]:
                    return go(p1, p2+1, p3+1)
                return False
            if p2 >= len(s2):
                if s1[p1] == s3[p3]:
                    return go(p1+1, p2, p3+1)
                return False

            one = go(p1+1, p2, p3+1) if s1[p1] == s3[p3] else False
            two = go(p1, p2+1, p3+1) if s2[p2] == s3[p3] else False

            memo[(p1, p2, p3)] = one or two

            return one or two

        return go(0, 0, 0)


def main():
    s = Solution()
    print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
    print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
    print(s.isInterleave('aaaaa' * 20, 'aaaaa' * 20, 'aaaaa' * 40))
    print(s.isInterleave('', '', ''))


if __name__ == '__main__':
    raise(SystemExit(main()))
