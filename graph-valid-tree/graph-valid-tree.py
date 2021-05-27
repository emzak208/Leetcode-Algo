from collections import deque 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        print(len(edges))
        if n == 0 or len(edges) != n - 1:
            return False 
        
        new_edges = []
        for start, end in edges:
            new_edges.append([start,end])
            new_edges.append([end,start])
            
        queue = deque([0])
        visited = set([0])
        
        while queue: 
            node = queue.popleft()
            for start, end in new_edges:
                if start == node and end not in visited:
                    queue.append(end)
                    visited.add(end)
        if len(visited) == n:
            return True 
        return False 
            
        
#     new_edges = []
#     for [a, b] in edges:
#       new_edges.append([a, b])
#       new_edges.append([b, a])
            
#     queue = deque([0])
#     visited = set([0])
#     while queue:
#       node = queue.popleft()
#       for [a, b] in new_edges:
#         if a == node and b not in visited:
#           visited.add(b)
#           queue.append(b)
    
#     if len(visited) == n:
#       return True
#     return False