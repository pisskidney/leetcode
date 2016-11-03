#!/usr/bin/python


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        xor = reduce(lambda x, y: x ^ y, nums, 0)
        check = xor & -xor
        n1, n2 = 0, 0
        for n in nums:
            if n & check:
                n1 ^= n
            else:
                n2 ^= n
        return n1, n2
            

s = Solution()
x = [1, 2, 4, 3, 2, 5, 1, 4]
print s.singleNumber(x)
