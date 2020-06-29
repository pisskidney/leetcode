# Given a collection of distinct integers, return all possible permutations.


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        numss = set(nums)
        def perm(numbers, current):
            if len(current) == len(numbers):
                res.append(current[:])
                return current
            for n in numbers:
                if n not in current:
                    current.append(n)
                    perm(numbers, current)
                    current.pop()
        perm(nums, [])
        return res


s = Solution()
a = [1, 2, 3]
print(s.permute(a))
