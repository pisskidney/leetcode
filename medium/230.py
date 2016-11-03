#!/usr/bin/python


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def kthSmallest(self, root, k):
        res, cnt = self.inorder(root, k, 0)
        return res

    def inorder(self, node, k, n):
        if not node:
            return None, n
        left_result, left_count = self.inorder(node.left, k, n)
        if left_result is not None:
            return left_result, 0
        current_count = left_count + 1
        if current_count == k:
            return node.val, current_count
        return self.inorder(node.right, k, current_count)
        

class SolutionIntByReferenceByContaineringIt(object):
    def kthSmallest(self, root, k):
        return self.inorder(root, k, [0])
        
    def inorder(self, node, k, n):
        if not node:
            return None
        left = self.inorder(node.left, k, n)
        if left is not None:
            return left
        n[0] += 1
        if n[0] == k:
            return node.val
        right = self.inorder(node.right, k, n)
        if right is not None:
            return right
        return None
        
t10 = TreeNode(10)
t5 = TreeNode(5)
t15 = TreeNode(15)
t4 = TreeNode(4)
t7 = TreeNode(7)
t3 = TreeNode(3)
t2 = TreeNode(0)
t6 = TreeNode(6)
t9 = TreeNode(9)
t12 = TreeNode(12)
t16 = TreeNode(16)

t10.left = t5
t10.right = t15
t5.left = t4
t5.right = t7
t4.left = t3
t3.left = t2
t7.left = t6
t7.right = t9
t15.left = t12
t15.right = t16

s = Solution()
print s.kthSmallest(t10, 17)

        
