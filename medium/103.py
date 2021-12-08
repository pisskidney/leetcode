"""
103. Binary Tree Zigzag Level Order Traversal

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root]]
        q = [root]
        while q:
            newq = []
            for node in q:
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            if newq:
                res.append(newq)
            q = newq
        res = [list(map(lambda x: x.val, row)) for row in res]
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        return res


def main():
    s = Solution()
    print(s.zigzagLevelOrder(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))


if __name__ == '__main__':
    raise(SystemExit(main()))
