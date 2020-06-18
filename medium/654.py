from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_max(self, start, end):
        maxnr = -1
        maxindex = -1
        for i in range(start, end + 1):
            if self.nums[i] > maxnr:
                maxnr = self.nums[i]
                maxindex = i
        return maxindex

    def build(self, start, end):
        if start > end:
            return None
        mid = self.get_max(start, end) 
        node = TreeNode(self.nums[mid])
        if mid > start:
            node.left = self.build(start, mid - 1)
        if mid < end:
            node.right = self.build(mid + 1, end)
        return node

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self.build(0, len(nums) - 1)


a = [3, 2, 1, 6, 0, 5]
s = Solution()
root = s.constructMaximumBinaryTree(a)
