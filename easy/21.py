#!/usr/bin/python


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        head = p1 if p1.val < p2.val else p2
        while p1 or p2:
            if p1.val < p2.val:
            else:
        return head

    def show(self, head):
        while head:
            print head.val,
            head = head.next
        print


s = Solution()
a, b = [], []
for i in range(1, 10, 2):
    a.append(ListNode(i))
    b.append(ListNode(i+1))
for i in xrange(len(a) - 1):
    a[i].next = a[i+1]
    b[i].next = b[i+1]
s.show(a[0])
s.show(b[0])
x = s.mergeTwoLists(a[0], b[0])
s.show(x)

