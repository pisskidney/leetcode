#!/usr/bin/python


from typing import Optional

"""
2. Add two numbers

https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode((l1.val + l2.val))
        cf = 1 if root.val >= 10 else 0
        root.val %= 10
        p = root
        p1, p2 = l1, l2

        while p1.next or p2.next:
            p.next = ListNode()
            p = p.next
            if p1.next:
                p1 = p1.next
                p.val += p1.val
            if p2.next:
                p2 = p2.next
                p.val += p2.val
            p.val += cf
            print(p.val)
            cf = 1 if p.val >= 10 else 0
            p.val %= 10

        if cf:
            p.next = ListNode(1, None)

        return root


def printlist(root):
    res = [root.val]
    p = root
    while (p := p.next):
        res.append(p.val)
    print(res)


def main():
    a = ListNode(8, ListNode(7, None))
    b = ListNode(8, ListNode(7, ListNode(9, ListNode(9, None))))

    s = Solution()
    printlist(s.addTwoNumbers(a, b))
    return 0


if __name__ == '__main__':
    raise SystemError(main())
