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
        p = root = ListNode((l1.val + l2.val) % 10)
        cf = 1 if l1.val + l2.val >= 10 else 0
        p1, p2 = l1, l2
        while (p1 and p1.next) or (p2 and p2.next) or cf:
            if p1 and p1.next:
                p1 = p1.next
            else:
                p1.val = 0
            if p2 and p2.next:
                p2 = p2.next
            else:
                p2.val = 0
            p.next = ListNode((p1.val + p2.val + cf) % 10)
            cf = 1 if p1.val + p2.val + cf >= 10 else 0
            p = p.next
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
