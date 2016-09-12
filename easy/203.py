#!/usr/bin/python


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        self.show(head)

        if not head:
            return
        while head is not None and head.val == val:
            q = head
            head = head.next
            del(q)
        p = head
        while p is not None and p.next is not None:
            if p.next.val == val:
                q = p.next
                p.next = p.next.next
                del(q)
            else:
                p = p.next

        self.show(head)

    def show(self, head):
        p = head
        while p is not None:
            print p.val,
            p = p.next
        print

'''
1->2->3->4->5

n1 = ListNode(3)
n2 = ListNode(3)
n3 = ListNode(3)
n4 = ListNode(3)
n5 = ListNode(1)
n6 = ListNode(3)
n7 = ListNode(3)
n8 = ListNode(3)
n9 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = None
'''
n1 = ListNode(1)

s = Solution()
s.removeElements(n1, 2)



