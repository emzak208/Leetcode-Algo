# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            next_queue = []
            res.append([node.val for node in queue]) # 每一层的一次性加进去
            for node in queue: # level order traversal 
                if node.left: 
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                queue = next_queue
        return res[::-1]
                
                