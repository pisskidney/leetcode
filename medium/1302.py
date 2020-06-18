
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '{}'.format(self.val)


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        res = 0
        while q:
            print(q)
            res = sum([node.val for node in q])
            newq = []
            for node in q:
                if node.left is not None:
                    newq.append(node.left)
                if node.right is not None:
                    newq.append(node.right)
            q = newq
        return res


btree = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]

def build_tree(i):
    if i >= len(btree) or btree[i] is None:
        return None
    return TreeNode(
        btree[i],
        build_tree(2 * i + 1),
        build_tree(2 * i + 2),
    )

root = build_tree(0)
print(root.right.right.right)
s = Solution()
print(s.deepestLeavesSum(root))
