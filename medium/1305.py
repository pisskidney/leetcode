# Given two binary search trees root1 and root2.
# Return a list containing all the integers from both trees sorted in ascending order.


 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1 = self.inorder(root1)
        tree2 = self.inorder(root2)
        i, j = 0, 0
        res = []
        while i < len(tree1) and j < len(tree2):
            if tree1[i] <= tree2[j]:
                res.append(tree1[i])
                i += 1
            else:
                res.append(tree2[j])
                j += 1
        if i < len(tree1):
            res += tree1[i:]
        elif j < len(tree2):
            res += tree2[j:]
        return res
