"""
95. Unique Binary Search Trees II

https://leetcode.com/problems/unique-binary-search-trees-ii/
"""
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode) -> None:
    q = deque([root])
    while q:
        row = []
        newq = deque()
        for elem in q:
            if elem.left:
                newq.append(elem.left)
            if elem.right:
                newq.append(elem.right)
            row.append(elem.val)
        q = newq
        print('   '.join(map(str, row)))


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def go(left, right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            res = []
            for i in range(left, right+1):
                leftvals = go(left, i-1)
                rightvals = go(i+1, right)
                for l in leftvals:
                    for r in rightvals:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return go(1, n)


def main():
    s = Solution()
    res = s.generateTrees(4)
    for r in res:
        inorder(r)
        print('-------')


if __name__ == '__main__':
    raise(SystemExit(main()))
