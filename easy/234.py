#!/usr/bin/python

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        import math

        if head is None or head.next is None:
            return True

        # get size
        size = 0
        curr = head
        while curr is not None:
            size += 1
            curr = curr.next

        # mid point
        mid_index = int(math.ceil(float(size) / 2))

        # go to mid - 1
        mid = head
        for _ in xrange(mid_index-1):
            mid = mid.next

        # reverse from mid to end
        before_mid = mid
        mid = mid.next
        curr = mid
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        before_mid.next = prev

        # start comparing head to mid mid_index 
        mid = prev
        while mid is not None:
            if head.val != mid.val:
                return False
            mid = mid.next
            head = head.next

        return True

    def show(self, head):
        while head is not None:
            print head.val,
            head = head.next
        print


nodes = [ListNode('a'),ListNode('b'),ListNode('c'),ListNode('a'),]
for i, node in enumerate(nodes[:-1]):
    node.next = nodes[i+1]
s = Solution()
print s.isPalindrome(nodes[0])





