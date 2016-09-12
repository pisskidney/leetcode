#!/usr/bin/python


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            if num not in h:
                h[num] = i
        for i, num in enumerate(nums):
            if target - num in h and h[target-num] != i:
                return i, h[target-num]
        return -1, -1
