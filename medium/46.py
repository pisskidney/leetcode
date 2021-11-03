from typing import List


"""
46. Permutations

https://leetcode.com/problems/permutations/
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def p(numbers, left, right):
            if left == right:
                res.append(numbers[:])
                return
            for i in range(left, right + 1):
                numbers[left], numbers[i] = numbers[i], numbers[left]
                p(numbers, left + 1, right)
                numbers[left], numbers[i] = numbers[i], numbers[left]
        p(nums, 0, len(nums) - 1)

        return res


def main():
    sol = Solution()
    print(sol.permute([1, 2, 3]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
