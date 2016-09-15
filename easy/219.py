#!/usr/bin/python


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h = {}
        for i, num in enumerate(nums):
            if num in h and i - h[num] <= k:
                return True
            h[num] = i
        return False


x = [1, 2, 3, 4, 5, 6, 7, 1]
k = 30
s = Solution()
print s.containsNearbyDuplicate(x, k)
