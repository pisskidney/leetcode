"""
145. Binary Tree Postorder Traversal

https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def go(node):
            if not node:
                return []
            go(node.left)
            go(node.right)
            res.append(node.val)

        go(root)
        return res


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
