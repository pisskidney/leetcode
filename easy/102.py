#!/usr/bin/python


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        res = [[root.val]]
        q = deque([])
        level = []
        q.append(root)
        while q or level:
            if not q:
                q = deque(level)
                res.append([x.val for x in level])
                level = []
            node = q.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        return res

s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print s.levelOrder(n1)
