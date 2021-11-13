#!/usr/bin/python
from typing import Optional


"""
61. Rotate List

https://leetcode.com/problems/rotate-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getlen(root: ListNode) -> int:
    n = 1
    p = root
    while p.next:
        n += 1
        p = p.next
    return n


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        n = getlen(head)
        k = k % n
        if not head.next or k == 0:
            return head

        i = 0
        p = head
        while i < n - k - 1:
            p = p.next
            i += 1

        res = p.next
        p.next = None

        p = res
        while p.next:
            p = p.next
        p.next = head

        return res


def main():
    sol = Solution()
    root = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    p = sol.rotateRight(root, 500000)
    p = sol.rotateRight(None, 0)
    while p:
        print(p.val)
        p = p.next
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
