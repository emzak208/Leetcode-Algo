"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque 

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        root = node
        if node is None:
            return node
        
        nodes = self.getNodes(node)
        mapping = {}
        for node in nodes: 
            mapping[node] = Node(node.val)
            
        for node in nodes: # can't combine 2 for loops, since nested for loop runs inside first  
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor] # find relationship from new
                new_node.neighbors.append(new_neighbor)
                
        return mapping[root]
                
    def getNodes(self, node):
        queue = deque([node]) # what if deque(node)
        result = set([node])
        
        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor) # 被visit过的
                    queue.append(neighbor) # 下一次要处理的
        return result 
                    
                
    
    
    
