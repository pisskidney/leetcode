#!/usr/bin/python


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from math import ceil
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.create(nums, 0, len(nums) - 1)

    def create(self, array, left, right):
        if left > right:
            return
        mid = int(ceil((left + right) / 2.0))
        node = TreeNode(array[mid])
        if left == right:
            return node
        node.left = self.create(array, left, mid - 1)
        node.right = self.create(array, mid + 1, right)
        return node


a = range(1, 8)
a = [1,3]
s = Solution()
print s.sortedArrayToBST(a)
