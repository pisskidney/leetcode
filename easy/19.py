#!/usr/bin/python


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        look = head
        for _ in xrange(n):
            look = look.next
        if look is None:
            q = head
            head = head.next
            del(q)
            return head
        p = head
        while look.next is not None:
            p = p.next
            look = look.next
        q, p.next = p.next, p.next.next
        del(q)
        return head

    def show(self, head):
        p = head
        while p is not None:
            print p.val,
            p = p.next
        print


n = 2
x = []
for i in xrange(n):
    x.append(ListNode(i+1))
for i, node in enumerate(x[:-1]):
    node.next = x[i+1]

s = Solution()
s.show(x[0])
h = s.removeNthFromEnd(x[0], 1)
s.show(h)


    
