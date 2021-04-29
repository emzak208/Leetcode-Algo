from collections import deque 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create a graph 
        graph = {i: [] for i in range(numCourses)} 
        in_degree = [0] * numCourses # position is the course number, eg in_degree[0] = course 0
        
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in) # key: node_out  
            in_degree[node_in] += 1 
        
        # initialize 
        queue = deque()
        num_choose = 0
        topo_sort = []
        
        # start to put nodes with in_degree == 0 in deque 
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i) # add course number 
                
        while queue:
            cur_course = queue.popleft()
            topo_sort.append(cur_course)
            num_choose += 1 
            for next_course in graph[cur_course]:
                in_degree[next_course] -= 1 
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        if num_choose == numCourses:
            return topo_sort     
                
                
#           graph = {0:[1,2], 1:[3], 2: [3]}
#           in_degree = [0,0,0,0] => [0,1,1,2]
        
                
        
                
        
            