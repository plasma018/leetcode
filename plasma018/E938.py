# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
      if root is None:
        return 0
      
      
      val = 0
      if root.val >= L:
        val += self.rangeSumBST(root.left, L, R)
      if root.val <= R:
        val += self.rangeSumBST(root.right, L, R)

      if root.val >= L and root.val <= R:
        return root.val + val
      
      return val
