# Given an n-ary tree, return the level order traversal of its nodes' values.


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        level = [root]
        while level:
            nextlevel = []
            vals = [node.val for node in level if node is not None]
            if vals:
                res.append(vals)
            for node in level:
                if node is not None:
                    nextlevel.extend(node.children)
            level = nextlevel
        return res
