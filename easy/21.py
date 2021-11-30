"""
21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        p = list1
        q = list2
        r = root
        while p and q:
            if p.val < q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next
            r = r.next
        if p:
            r.next = p
        if q:
            r.next = q
        return root.next



def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
