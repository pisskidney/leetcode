"""
110. Balanced Binary Tree

https://leetcode.com/problems/balanced-binary-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def go(node):
            if not node:
                return 1, 1

            left = go(node.left)
            right = go(node.right)

            if not all([left, right]):
                return False

            leftmin, leftmax = left
            rightmin, rightmax = right

            if abs(leftmin - rightmax) > 1 or abs(leftmax - rightmin) > 1:
                return False

            return min(leftmin, rightmin) + 1, max(leftmax, rightmax) + 1

        res = go(root)
        return res is not False


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
