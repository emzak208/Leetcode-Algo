# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenTree(self, node):
        if not node:
            return None
        
        # return if not 
        if not node.left and not node.right:
            return node
        
        leftTail = self.flattenTree(node.left) # the tail node of the flatten left subtree
        rightTail = self.flattenTree(node.right) # the tail node of the flatten right subtree
        
        # if there's a left tree, we shuffle the connections arouns so that there are no left tree
        if leftTail:
            leftTail.right = node.right  # connect left & right subtree
            node.right = node.left 
            node.left = None
            
        # we need to return the right most node after we are done writing the new connections 
        return rightTail if rightTail else leftTail 
    
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.flattenTree(root)

        
        