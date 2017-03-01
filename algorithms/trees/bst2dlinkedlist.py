#!/usr/bin/python


class Node:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


class ListNode:
    def __init__(self, prev, next, val):
        self.prev = prev
        self.next = next
        self.val = val


def bst2list(node):
    if node is None:
        return None, None
    lleft, lright = bst2list(node.left)
    rleft, rright = bst2list(node.right)
    n = ListNode(lright, rleft, node.val)
    if lright is not None:
        lright.next = n
    if rleft is not None:
        rleft.prev = n
    lleft = lleft or n
    rright = rright or n
    return lleft, rright


a = [5, 3, 7, 2, 4, 6, 8]
tree = [None for _ in xrange(max(a) + 1)]
for x in a:
    tree[x] = Node(None, None, x)
tree[5].left = tree[3]
tree[5].right = tree[7]
tree[3].left = tree[2]
tree[3].right = tree[4]
tree[7].left = tree[6]
tree[7].right = tree[8]


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print node.val
    inorder(node.right)

#inorder(tree[5])
x, y = bst2list(tree[5])
while x:
    print x.val
    x = x.next




