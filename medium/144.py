#!/usr/bin/python


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


s = Solution()
a = []
for i in xrange(1, 16):
    a.append(TreeNode(i))
for i in xrange(len(a)):
    if 2*i+1 < len(a):
        a[i].left = a[2*i+1]
    if 2*i+2 < len(a):
        a[i].right = a[2*i+2]
print s.preorderTraversal(a[0])
