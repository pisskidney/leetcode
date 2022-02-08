"""
109. Convert Sorted List to Binary Search Tree

https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return (
            f'     {self.val}\n'
            f'   /   \\\n'
            f'{self.left.val if self.left else None}    '
            f'{self.right.val if self.right else None}\n'
        )


def inorder(head):
    if head is None:
        return
    inorder(head.left)
    print(head.val)
    inorder(head.right)


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def go(l, r):
            print(l, r)
            if l is None and r is None:
                return TreeNode(l.val)

            if l is None:
                return TreeNode(r.val)

            if r is None:
                return TreeNode(l.val)

            if l is r:
                return TreeNode(l.val)

            prev = None
            slow = l
            fast = l
            while fast != r and fast.next and fast.next != r and fast.next.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            node = TreeNode(slow.val)
            if prev is not None:
                node.left = go(l, prev)
            node.right = go(slow.next, r)

            return node

        if not head:
            return None

        last = head
        while last.next:
            last = last.next

        return go(head, last)


def main():
    s = Solution()
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    inorder(s.sortedListToBST(a))
    inorder(s.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))))


if __name__ == '__main__':
    raise(SystemExit(main()))
