"""
148. Sort List

https://leetcode.com/problems/sort-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def printl(head: Optional[ListNode]) -> None:
    acc = []
    while head:
        acc.append(head)
        head = head.next
    print(acc)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        def combine(head1, head2):
            p, q = head1, head2
            root = ListNode(0)
            r = root
            while p or q:
                if p and q:
                    if p.val <= q.val:
                        r.next = p
                        p = p.next
                    else:
                        r.next = q
                        q = q.next
                elif p:
                    r.next = p
                    p = p.next
                else:
                    r.next = q
                    q = q.next
                r = r.next
            r.next = None
            return root.next

        def mergesort(left, right):
            if not left or not right:
                if not left:
                    return right
                if not right:
                    return left
            if left == right:
                return left

            mid, fast = left, left
            while (
                fast.next and
                fast.next.next and
                fast != right and
                fast.next != right and
                fast.next.next != right
            ):
                mid = mid.next
                fast = fast.next.next

            left2 = mid.next
            mid.next = None
            right.next = None

            left = mergesort(left, mid)
            right = mergesort(left2, right)
            return combine(left, right)

        right = head
        while right.next:
            right = right.next

        return mergesort(head, right)


def main():
    s = Solution()

    a = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    printl(a)
    printl(s.sortList(a))

    a = ListNode(4, ListNode(2, ListNode(1, ListNode(3, ListNode(0)))))
    printl(a)
    printl(s.sortList(a))

    a = ListNode(4)
    printl(a)
    printl(s.sortList(a))

    a = None
    printl(a)
    printl(s.sortList(a))


if __name__ == '__main__':
    raise(SystemExit(main()))
