# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.


from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        count = 0
        d = {0: 0}
        for i, n in enumerate(nums, 1):
            count += n or -1
            if count in d:
                res = max(res, i - d[count])
            else:
                d[count] = i
        return res


s = Solution()
print(s.findMaxLength([0, 1, 1, 1, 0, 0]))
print(s.findMaxLength([1, 1, 1, 0, 1, 1]))
print(s.findMaxLength([1, 1, 1]))
