#!/usr/bin/python


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        newhead = self.recursive(None, head)
        return newhead

    def iterative(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def recursive(self, prev, cur):
        next = cur.next
        cur.next = prev
        if next is not None:
            return self.recursive(cur, next)
        else:
            return cur

    def show(self, head):
        while head is not None:
            print head.val,
            head = head.next


nodes = []
for i in xrange(10):
    n = ListNode(i+1)
    nodes.append(n)

for i, node in enumerate(nodes[:-1]):
    node.next = nodes[i+1]

s = Solution()
s.show(nodes[0])
s.iterative(nodes[0])
s.show(nodes[-1])
