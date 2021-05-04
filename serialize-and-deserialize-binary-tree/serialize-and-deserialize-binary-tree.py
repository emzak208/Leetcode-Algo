# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else 'null')
            if node: 
                queue.append(node.left)
                queue.append(node.right)
        
        # return bfs_order 
        return ' '.join(bfs_order)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # convert string into a list,where each element is a TreeNode object 
        if not data:
            return None

        bfs_order = [
            TreeNode(int(val)) if val != 'null' else None
            for val in data.split()
        ]
        root = bfs_order[0]
        fast_index = 1
        
        nodes, slow_index = [root], 0
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        
        return root
#         bfs_order = [TreeNode(int(val)) if val != 'null' else None for val in data.split()] 
#         # print(nodes)
#         root = bfs_order[0]
#         slow_idx, fast_idx = 0, 1
        
#         node = [root]
#         while slow_idx < len(bfs_order):
#             node = bfs_order[slow_idx]
#             slow_idx += 1 
#             if node: 
#                 node.left = bfs_order[fast_idx]
#                 node.right = bfs_order[fast_idx + 1]
#                 fast_idx += 2 
        
#         return root 
                
                
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))