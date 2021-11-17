"""
82. Remove Duplicates from Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        root = ListNode()
        q = root
        avoid = None
        while p is not None:
            if p.val == avoid:
                p = p.next
                continue
            if p.next and p.next.val == p.val:
                avoid = p.val
                p = p.next
                continue
            q.next = p
            q = q.next


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
