#!/usr/bin/python


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        if not root:
            return []
        level = deque([root])
        res = []
        while level:
            res.append(level[-1].val)
            nextlevel = []
            while level:
                node = level.popleft()
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            level = deque(nextlevel)
        return res


a = [3, 5, 4, 1, 2, None, None, None, 7, None, 5, None, None, None, None, None, None, None, 9]
b = [TreeNode(x) if x else None for x in a]

for i in xrange(len(a)/2):
    if b[i]:
        b[i].left = b[i*2+1]
        b[i].right = b[i*2+2]

s = Solution()
print s.rightSideView(b[0])

        
