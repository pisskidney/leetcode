#!/usr/bin/python


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        current = []
        self.go(root, current, res)
        print res

    def go(self, node, current, res):
        current = current[:]
        current.append(str(node.val))
        if not node.left and not node.right:
            res.append('->'.join(current))
        else:
            if node.left:
                self.go(node.left, current, res)
            if node.right:
                self.go(node.right, current, res)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)


n1.left = n2
n1.right = n3
n2.left = n5
n3.left = n4
n3.right = n5

s = Solution()
s.binaryTreePaths(n1)
            
        
        
