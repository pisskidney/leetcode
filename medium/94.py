#!/usr/bin/python


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        visited = {}
        res = []
        while stack:
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
            else:
                node = stack.pop()
                res.append(node.val)
                visited[node] = True
                if node.right and node.right not in visited:
                    stack.append(node.right)
        return res


t1 = TreeNode(5)
t2 = TreeNode(3)
t3 = TreeNode(9)
t4 = TreeNode(1)
t5 = TreeNode(4)
t6 = TreeNode(6)
t7 = TreeNode(12)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7

s = Solution()
s.inorderTraversal(t1)
