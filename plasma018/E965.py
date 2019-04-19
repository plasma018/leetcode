# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        _bool = True
        if root.right != None:
            if root.val == root.right.val:
                _bool = self.isUnivalTree(root.right)
            else:
                return False
        if _bool and root.left != None:
            if root.val == root.left.val:
                _bool = self.isUnivalTree(root.left)
            else:
                return False
        return _bool
