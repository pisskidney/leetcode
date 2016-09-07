#!/usr/bin/python


class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.sums = []
        summ = 0
        for i in xrange(len(nums)):
            summ += self.nums[i]
            self.sums.append(summ)
            

    def sumRange(self, i, j):
        if i == j:
            return self.nums[i]
        if i > j:
            return 0
        if i < 0 or i >= len(self.nums):
            return 0
        previous_sum = self.sums[i - 1] if i - 1 >= 0 else 0
        return self.sums[j] - previous_sum


x = [1, -1, 2, -3, 4, 5, 2, -1]
s = NumArray(x)
assert s.sumRange(0, 0) == 1
assert s.sumRange(0, 2) == 2
assert s.sumRange(3, 7) == 7
