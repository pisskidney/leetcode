#!/usr/bin/python


class Node():
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.children = {}


class Solution():
    def buildTree(self, dump):
        self.root = Node(None)
        for stack in dump:
            current = self.root
            for s in stack:
                if s not in current.children:
                    current.children[s] = Node(s)
                else:
                    current.children[s].count += 1
                current = current.children[s]

    def show(self):
        self.rec(self.root, 0)

    def rec(self, node, level):
        print ' ' * level, node.val, ' - ', node.count
        for n in node.children.values():
            self.rec(n, level+1)


dump = [
    ['f1', 'f2', 'f3'],
    ['f1', 'f3', 'f5'],
]


s = Solution()
s.buildTree(dump)
s.show()
