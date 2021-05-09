from collections import deque 
directions = [(0,1), (0,-1), (1,0), (-1,0)]

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0] or start == destination:
            return False 
        
        queue = deque([(start[0],start[1])])
        visited = set() # 记录访问过的点
        m, n = len(maze),len(maze[0])
        
        while queue: 
            x, y = queue.popleft()  
            visited.add((x, y))
            if (x, y) == (destination[0],destination[1]):
                return True 
            
            for delta_x, delta_y in directions: 
                x_, y_ = x, y
                while 0<=x_+delta_x<m and 0<=y_+delta_y<n and maze[x_+delta_x][y_+delta_y] == 0:
                    x_ = x_ + delta_x
                    y_ = y_ + delta_y
                if (x_, y_) not in visited:
                    queue.append((x_, y_))
        
        return False 
        
        
 