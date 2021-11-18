"""
82. Remove Duplicates from Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printx(head: Optional[ListNode]) -> None:
    p = head
    res = []
    while p is not None:
        res.append(p.val)
        p = p.next
    print(res)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prev = None
        root = ListNode()
        q = root
        while p is not None:
            if (p.next is None or p.next.val != p.val) and (prev is None or prev.val != p.val):
                q.next = p
                q = q.next
            prev = p
            p = p.next
        q.next = None
        return root.next


def main():
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    printx(head)
    printx(s.deleteDuplicates(head))
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(5)))))
    printx(head)
    printx(s.deleteDuplicates(head))
    head = ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(5)))))
    printx(head)
    printx(s.deleteDuplicates(head))
    head = ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(5, ListNode(5))))))
    printx(head)
    printx(s.deleteDuplicates(head))
    head = ListNode(2)
    printx(head)
    printx(s.deleteDuplicates(head))
    head = None
    printx(head)
    printx(s.deleteDuplicates(head))


if __name__ == '__main__':
    raise(SystemExit(main()))
