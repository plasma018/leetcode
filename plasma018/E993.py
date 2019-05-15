# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
      
      def depth(node, x, depths, deep):
        if node is None:
          return None
        
        if node.val is x:
          depths.append(deep)
          return 1
        
        nodeL = depth(node.left, x, depths, deep+1)    
        if nodeL == 1:
          return node
        nodeR = depth(node.right, x, depths, deep+1)
        if nodeR == 1:
          return node
        return nodeL or nodeR
      
      depths = []
      
      nodeL = depth(root, x, depths, 0)
      nodeR = depth(root, y, depths, 0)

      return depths[0] == depths[1] and nodeL is not nodeR
