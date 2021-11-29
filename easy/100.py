"""
100. Same Tree

https://leetcode.com/problems/same-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if any([q is None, p is None]):
            if not all([q is None, p is None]):
                return False
            return True
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def main():
    s = Solution()
    print(s.isSameTree(None, None))
    print(s.isSameTree(TreeNode(2), TreeNode(2)))
    print(s.isSameTree(TreeNode(3), TreeNode(2)))


if __name__ == '__main__':
    raise(SystemExit(main()))
