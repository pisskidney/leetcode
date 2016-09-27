#!/usr/bin/python


class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)
        if len(nums) < 3:
            return max(nums)
        self.mem = {}
        return self.rec(len(nums)-1, nums)

    def rec(self, i, nums):
        if i == 0:
            return nums[0]
        elif i == 1:
            return max(nums[0], nums[1])
        if i in self.mem:
            return self.mem[i]
        self.mem[i] = nums[i] + self.rec(i-2, nums) if nums[i] + self.rec(i-2, nums) > self.rec(i-1, nums) else self.rec(i-1, nums)

        return self.mem[i]



class SolutionBottomUp(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in xrange(1, len(nums)):
            if dp[i-2] + nums[i] > dp[i-1]:
                dp[i] = dp[i-2] + nums[i]
            else:
                dp[i] = dp[i-1]
        return dp[-1]


s = Solution()
nums = [3, 2, 1]
print s.rob(nums)
