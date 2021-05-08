from collections import deque

# BFS 思路：
# 1. use a queue to track current position and distance from the start 
# 2. keep updating a visited dic to where key is (x,y) is positions, values is shortest path 
# 3. return result from visited 

directions = [(1,0), (-1,0), (0,-1), (0,1)]

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0] or start == destination:
            return 0
        
        m, n = len(maze), len(maze[0]) # rows, cols 
        visited = {(start[0],start[1]): 0} # initialize distance 0
        queue = deque([(start[0],start[1], 0)]) # position & distance from start 
        
        while queue:
            x, y, dist = queue.popleft()
            
            for delta_x, delta_y in directions:
                i, j, d = x, y, dist
                while 0<=i+delta_x<m and 0<=j+delta_y<n and maze[i+delta_x][j+delta_y] == 0: # only when see "0" 
                    i += delta_x
                    j += delta_y
                    d += 1 
                    
                # update visited: if from start to a certain point have multiple ways, update w.the shortest
                if (i, j) not in visited or ((i, j) in visited and visited[(i, j)] > d):
                    visited[(i, j)] = d
                    if (i, j) != (destination[0], destination[1]):
                        queue.append((i, j, d))
                        
        return visited.get((destination[0], destination[1]), -1)
        
#          visited.get((destination[0], destination[1]), -1)
                    
            
            