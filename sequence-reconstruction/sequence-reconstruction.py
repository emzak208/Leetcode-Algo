from collections import deque 

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # create gragh 
        graph = {}
        for seq in seqs:
            for node in seq: 
                if node not in graph:
                    graph[node] = set()
        
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i]) # 每个key的value是后一个数<=>图中每个数指向后一个数
        print(graph)
        
        # calculate in_degree
        in_degree = {node: 0 for node in graph} # in_degree for every key(node) in graoh
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1 
        print(in_degree)
        
        # BFS 
        queue = deque()
        for node in graph:
            if in_degree[node] == 0:
                queue.append(node)
                
        topo_sort = []
        while queue: 
            if len(queue) > 1: # if more than 1 node have in_degree == 0 => must have more than 1 top sort
                return False
            
            node = queue.popleft()
            topo_sort.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        print(topo_sort)
        return len(org) == len(graph) and org == topo_sort
            

                    
            