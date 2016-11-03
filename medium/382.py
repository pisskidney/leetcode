#!/usr/bin/python

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from random import randint
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = self.head
        i = 1
        p = self.head.next
        while p:
            if randint(0, i) == 0:
                res = p
            i += 1
            p = p.next
        return res.val

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
s = Solution(l1)
print s.getRandom()
