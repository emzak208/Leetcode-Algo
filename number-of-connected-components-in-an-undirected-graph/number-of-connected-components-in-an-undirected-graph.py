# 类似于问有几个island <=> 问能做几遍BFS
from collections import deque 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges or n == 0:
            return n 
        
        new_edges = []
        for start, end in edges:
            new_edges.append([start,end])
            new_edges.append([end,start])
        
        queue = deque([0])
        visited = set([0])
        res = 1
        
        for index in range(n):
            if index not in visited: 
                queue.append(index)
                res += 1 
            while queue: 
                node = queue.popleft()
                for start, end in new_edges:
                    if start == node and end not in visited:
                        queue.append(end)
                        visited.add(end)
           
               
        return res
                    
        
        
        