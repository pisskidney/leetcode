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

        def go(node, imin, imax):

            if not node:
                return

            if imin[0] is not None and imin[0] >= node.val:
                node.val, imin[1].val = imin[1].val, node.val
                return
            elif imax[0] is not None and imax[0] <= node.val:
                node.val, imax[1].val = imax[1].val, node.val
                return

            go(node.left, imin, (node.val, node) if imax[0] is None or node.val < imax[0] else imax)
            go(node.right, (node.val, node) if imin[0] is None or node.val > imin[0] else imin, imax)

        go(root, (None, None), (None, None))
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
