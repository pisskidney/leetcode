"""
86. Partition List

https://leetcode.com/problems/partition-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printl(head: Optional[ListNode]) -> None:
    acc = []
    while head:
        acc.append(head.val)
        head = head.next
    print(acc)


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = p = ListNode(0)
        h = q = ListNode(0)
        while head:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next
        p.next = h.next
        q.next = None
        return l.next


class SolutionBad:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        k = n = moved = 0
        p = head
        while p:
            n += 1
            p = p.next
        p = head
        while k < n - moved:
            if p.val >= x:
                moved += 1
                q = p
                while q.next:
                    q.val, q.next.val = q.next.val, q.val
                    q = q.next
            else:
                p = p.next
                k += 1
        return head


def main():
    s = Solution()
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    printl(head)
    printl(s.partition(head, 3))


if __name__ == '__main__':
    raise(SystemExit(main()))
