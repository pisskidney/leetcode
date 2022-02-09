"""
114. Flatten Binary Tree to Linked List

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def go(node):
            if node is None:
                return None
            if node.left is None and node.right is None:
                return None
            go(node.left)
            go(node.right)

            if node.left is None:
                return

            save_right = node.right
            node.right = node.left
            node.left = None
            last_right = node.right
            while last_right.right is not None:
                last_right = last_right.right
            last_right.right = save_right
        go(root)


def main():
    s = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    # root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    s.flatten(root)
    while root:
        print(root.val)
        root = root.right


if __name__ == '__main__':
    raise(SystemExit(main()))
