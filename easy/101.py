#!/usr/bin/python


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        left = []
        right = []
        self.go(root.left, left)
        self.go(root.right, right)
        return left == right[::-1]

    def go(self, root, res):
        if root:
            self.go(root.left, res)
            res.append(root.val)
            self.go(root.right, res)

class SolutionIterative(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = [root.left]
        right = [root.right]
        while any(left) or any(right):
            if [x.val if x is not None else None for x in left] != [x.val if x is not None else None for x in right][::-1]:
                return False
            newleft, newright = [], []
            for l in left:
                if l is not None:
                    newleft.append(l.left)
                    newleft.append(l.right)
            for r in right:
                if r is not None:
                    newright.append(r.left)
                    newright.append(r.right)
            left, right = newleft, newright
        return True

            
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(3)
n7 = TreeNode(4)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n7
n3.right = n6

s = Solution()
print s.isSymmetric(n1)
        
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(2)
n4 = TreeNode(3)
n5 = TreeNode(3)
n1.left = n2
n1.right = n3
n2.right = n4
n3.left = n5

print s.isSymmetric(n1)
