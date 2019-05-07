# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.help(root, 0)
        return root
    
    def help(self, root, head):
        if root == None:
            return head 
        
        right = self.help(root.right, head)
        
        root.val += right
        self.help(root.left, root.val)
        return self.left(root)
    
    def left(self, node):
        val = node.val
        if node.left is not None:
            val = self.left(node.left)
        return val
