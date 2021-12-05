"""
104. Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def maxx(node, level):
            if not node:
                return level - 1
            return max(maxx(node.left, level+1), maxx(node.right, level+1))

        return maxx(root, 1)


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
