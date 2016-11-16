#!/usr/bin/python


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        p, res, prev = head, p.next, ListNode(0)
        while p and p.next:
            p.next.next, p.next, prev.next, prev, p = p, p.next.next, p.next, p, p.next.next
        return res


a = range(1, 5)
b = []
for i in a:
    b.append(ListNode(i))
for i in xrange(len(b) - 1):
    b[i].next = b[i+1]
s = Solution()
x = s.swapPairs(b[0])
while x:
    print x.val
    x = x.next

