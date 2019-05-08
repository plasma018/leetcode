# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        array1 = []
        array2 = []
        
        self.helper(root1, array1)
        self.helper(root2, array2)

        return array1 == array2
        
    def helper(self, root, array):
        
        if root is None:
            return 
        
        if root.left is None and root.right is None:
            array.append(root.val)
            return 
            
        self.helper(root.left, array)
        
        self.helper(root.right, array)
