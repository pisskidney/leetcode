#!/usr/bin/python


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        from copy import copy
        if not root:
            return 0
        q = deque([])
        tempq = deque([])
        q.append(root)
        c = 1
        while True:
            if not q:
                q = copy(tempq)
                tempq = deque([])
                c += 1
            node = q.popleft()
            if not node.left and not node.right:
                return c
            else:
                if node.left:
                    tempq.append(node.left)
                if node.right:
                    tempq.append(node.right)


n1 = TreeNode(1)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 = TreeNode(1)
n5 = TreeNode(1)
n6 = TreeNode(1)
n7 = TreeNode(1)

n1.right = n2
n2.right = n3
n3.right = n4
n4.right = n5
n5.right = n6
n6.right = n7

s = Solution()
print s.minDepth(n1)

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(1)
n6 = TreeNode(1)
n7 = TreeNode(1)

n1.right = n3
n1.left = n2
n2.left = n4

s = Solution()
print s.minDepth(n1)
