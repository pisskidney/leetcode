#!/usr/bin/python


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class SolutionIterative(object):
    def deleteDuplicates(self, head):



class SolutionIterative(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head.next
        prev = head
        while p is not None:
            if p.val == prev.val:
                prev.next = p.next
            else:
                prev = prev.next
            p = p.next
        return head
            
        
