"""
99. Recover Binary Search Tree

https://leetcode.com/problems/recover-binary-search-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printx(root: TreeNode) -> None:
    q = [root]
    while q:
        newq = []
        row = []
        for elem in q:
            row.append(elem.val)
            if elem.left is not None:
                newq.append(elem.left)
            if elem.right is not None:
                newq.append(elem.right)
        print(row)
        q = newq


class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None

        def go(node):
            if not node:
                return

            go(node.left)

            if not self.first and self.prev.val >= node.val:
                self.first = self.prev
            if self.first and self.prev.val >= node.val:
                self.second = node
            self.prev = node

            go(node.right)

        print(self.first, self.second)

        return root


def main():
    s = Solution()
    a = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    printx(a)
    printx(s.recoverTree(a))

    print('----------')

    a = TreeNode(2, TreeNode(3, TreeNode(1)))
    printx(a)
    printx(s.recoverTree(a))


if __name__ == '__main__':
    raise(SystemExit(main()))
