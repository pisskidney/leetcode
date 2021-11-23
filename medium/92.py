"""
92. Reverse Linked List II

https://leetcode.com/problems/reverse-linked-list-ii/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printx(head: ListNode) -> None:
    acc = []
    while head:
        acc.append(head.val)
        head = head.next
    print(acc)


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        root = ListNode(0)
        root.next = head
        i = 0
        p = head
        prevp = root

        while p:
            if i + 1 == left:
                q = p
                prevq = None

                for _ in range(right - left + 1):
                    nextq = q.next
                    if prevq is not None:
                        q.next = prevq
                    prevq = q
                    q = nextq

                prevp.next = prevq
                p.next = q

            prevp = p
            p = p.next
            i += 1

        return root.next


def main():
    s = Solution()
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    a = ListNode(1, ListNode(2))
    printx(a)
    printx(s.reverseBetween(a, 1, 2))


if __name__ == '__main__':
    raise(SystemExit(main()))
