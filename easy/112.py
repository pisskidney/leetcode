#!/usr/bin/python


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.go(root, 0, sum)

    def go(self, node, current_sum, sum):
        print node.val
        current_sum += node.val
        a, b = False, False
        if node.left:
            a = self.go(node.left, current_sum, sum)
        if node.right:
            b = self.go(node.right, current_sum, sum)
        elif not node.left:
            if current_sum == sum:
                return True
            else:
                return False
        return a or b


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)

n5.left = n4
n5.right = n8
n4.left = n6
n6.left = n7
n6.right = n2
n8.left = n3
n8.right = n9
n9.right = n1

s = Solution()
print s.hasPathSum(n5, 17)
