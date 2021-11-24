"""
98. Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def go(node, imin, imax):
            if not node:
                return True
            if (
                (node.left and node.left.val >= node.val) or
                (node.right and node.right.val <= node.val)
            ):
                return False
            if imax and node.val >= imax:
                return False
            if imin and node.val <= imin:
                return False

            return (
                go(node.left, imin, min(imax, node.val) if imax is not None else node.val) and
                go(node.right, max(imin, node.val) if imin is not None else node.val, imax)
            )

        return go(root, None, None)


def main():
    s = Solution()
    print(s.isValidBST(TreeNode(0, TreeNode(-1))))


if __name__ == '__main__':
    raise(SystemExit(main()))
