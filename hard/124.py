"""
124. Binary Tree Maximum Path Sum

https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    res = -(10**20)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.go(root.left)
        right = self.go(root.right)

        return max(left + right + root.val, root.val, self.res, root.val + left, root.val + right)

    def go(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.go(root.left)
        right = self.go(root.right)

        maxOne = max(root.val, left + root.val, right + root.val)
        maxAll = max(maxOne, left + right + root.val)

        self.res = max(self.res, maxAll)

        return maxOne


def main():
    s = Solution()
    print(s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(s.maxPathSum(TreeNode(2, TreeNode(-1))))


if __name__ == '__main__':
    raise(SystemExit(main()))
