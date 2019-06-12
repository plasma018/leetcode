# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
      def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        num = self.helper(root, limit, 0)
        return  None if num < limit else root
      
      def helper(self, root: TreeNode, limit: int, amount: int):
        
        if root.left is None and root.right is None:
          return amount + root.val
        
        left, right = 0, 0
        if root.left is not None:
          left = self.helper(root.left, limit, amount+root.val)
          if left < limit:
            root.left = None
          
        if root.right is not None:
          right = self.helper(root.right, limit, amount+root.val)
          if right < limit:
            root.right = None
        
        if (root.right is None and left < limit) or (root.left is None and right < limit):
          return limit - 1
        
        return  left if left > right else right
