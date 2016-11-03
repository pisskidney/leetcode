#!/usr/bin/python


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return 0
        return self.traverse(root, sum)

    def findPathSum(self, node, sum, csum):
        if not node:
            return 0
        csum += node.val
        if csum == sum:
            return 1 + self.findPathSum(node.left, sum, csum) + self.findPathSum(node.right, sum, csum)
        return self.findPathSum(node.left, sum, csum) + self.findPathSum(node.right, sum, csum)

    def traverse(self, node, sum):
        if not node:
            return 0
        return self.findPathSum(node, sum, 0) + self.traverse(node.left, sum) + self.traverse(node.right, sum)


class SolutionRecursiveNotOk(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        from collections import deque
        q = deque([])
        return self.sums(root, sum, q, 0)
    
    def sums(self, node, sum, q, qsum):
        if not node:
            return 0
        q.append(node.val)
        qsum += node.val
        while abs(qsum) > sum:
            print node.val
            x = q.popleft()
            qsum -= x
        if qsum == sum:
            return 1 + self.sums(node.left, sum, q, qsum) + self.sums(node.right, sum, q, qsum)
        return self.sums(node.left, sum, q, qsum) + self.sums(node.right, sum, q, qsum)
            

s = Solution()
a = [10,5,-3,3,2,None,11,3,-2,None,1]
b = []
for i in xrange(len(a)):
    if a[i] is not None:
        b.append(TreeNode(a[i]))
    else:
        b.append(None)
    
for i in xrange(len(a)/2):
    b[i].left = b[i*2+1] if i*2+1 < len(a) else None
    b[i].right = b[i*2+2] if i*2+2 < len(a) else None

print s.pathSum(b[0], 8)
