#!/usr/bin/python


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        odd, podd, even, peven = head, head, head.next, head.next
        isodd = True
        p = even.next
        while p:
            podd.next = p
            podd = podd.next
            peven.next = p.next
            peven = peven.next
            p = p.next
        podd.next = even
        peven.next = None
        return odd

    def show(self, head):
        p = head
        while p:
            print p.val, 
            p = p.next
        print 
        

a = []
for i in xrange(3):
    a.append(ListNode(i+1))
for i in xrange(len(a) - 1):
    a[i].next = a[i+1]
s = Solution()
s.show(a[0])
x = s.oddEvenList(a[0])
s.show(x)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
