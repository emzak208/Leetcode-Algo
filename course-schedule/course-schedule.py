from collections import deque 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        
        # create the graph
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in) # graph without starting node 
            in_degree[node_in] += 1 # position is the course num
        # print(in_degree)
        
        num_choose = 0
        queue = deque()
        
        # 将入度为零的放入队列
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i) # append course number 
                
        while queue: 
            curr_pos = queue.popleft()
            num_choose += 1 # course number 
            for next_pos in graph[curr_pos]:
                in_degree[next_pos] -= 1 
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
                    
        return num_choose == numCourses
            
            
            
            