# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
      left, right = None, None
      
      if root.left is not None:
        left = self.increasingBST(root.left)
        prev = left
        while prev.right != None:
          prev = prev.right
        prev.right = root
        root.left = None
        
      if root.right is not None:
        right = self.increasingBST(root.right)
        root.right = right
      
      return root if left is None else left
