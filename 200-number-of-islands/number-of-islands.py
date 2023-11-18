from collections import deque 
directions = [(0,1),(-1,0),(0,-1),(1,0)] # up, left, down, right 

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        n_island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited: # only bfs when sees '1'
                    self.bfs(grid, visited, i, j)
                    n_island += 1 
        return n_island
        
    def bfs(self, grid, visited, x, y):
        queue = deque([(x,y)])
        visited.add((x,y))
        
        while queue:
            x, y = queue.popleft()
            visited.add((x, y))
            for delta_x, delta_y in directions:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue 
                queue.append((next_x,next_y))
                visited.add((next_x,next_y))
       
    def is_valid(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] == "1" # pay attention, some questions values in grid are numeric
    

        