"""
975. Range Sum of BST

https://leetcode.com/problems/range-sum-of-bst/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def go(node):
            if not node:
                return 0
            left = go(node.left) if node.val > low else 0
            right = go(node.right) if node.val < high else 0
            this = node.val if low <= node.val <= high else 0
            return this + left + right

        return go(root)


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
