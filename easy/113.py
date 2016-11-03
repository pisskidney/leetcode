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
            return []
        return self.paths(root, sum)


    def paths(self, node, sum):
        if not node.left and not node.right:
            if node.val == sum:
                return [[node.val]]
            else:
                return []
        left, right = [], []
        if node.left:
            left = self.paths(node.left, sum-node.val)
        if node.right:
            right = self.paths(node.right, sum-node.val)
        return [[node.val] + i for i in left + right]



class Solution2(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        return self.paths(root, [], sum)

    def paths(self, node, path, summ):
        path.append(node.val)
        if not node.left and not node.right:
            if sum(path) == summ:
                return [path[:]]
            else:
                return []
        left, right = [], []
        if node.left:
            left = self.paths(node.left, path, summ)
            path.pop()
        if node.right:
            right = self.paths(node.right, path, summ)
            path.pop()
        return left + right


s = Solution()
a = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
b = []
for i in xrange(len(a)):
    if a[i] is not None:
        b.append(TreeNode(a[i]))
    else:
        b.append(None)
    
for i in xrange(len(a)/2):
    if b[i]:
        b[i].left = b[i*2+1] if i*2+1 < len(a) else None
        b[i].right = b[i*2+2] if i*2+2 < len(a) else None

print s.pathSum(b[0], 22)
