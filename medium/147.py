"""
147. Insertion Sort List

https://leetcode.com/problems/insertion-sort-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = head
        p = head.next
        while p:
            if p.val < prev.val:
                whatnext = p.next

                prev.next = p.next
                root = ListNode(0, head)
                q = root
                while q.next.val < p.val:
                    q = q.next
                p.next = q.next
                q.next = p
                head = root.next

                p = whatnext
            else:
                prev = p
                p = p.next

        return head


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
