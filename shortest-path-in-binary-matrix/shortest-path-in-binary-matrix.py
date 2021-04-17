from collections import deque 
directions = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        for r in grid:
            print(r)
        distance = {(0,0): 1}
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
                
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1 
        
        # bfs
        queue = deque([(0, 0)])
        
        while queue: 
            x, y = queue.popleft()
            if (x, y) == (max_row, max_col): 
                return distance[(x ,y)]
            for delta_x, delta_y in directions: 
                next_x = x + delta_x
                next_y = y + delta_y
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue 
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))
        print('Q exhausted')
        return -1
    
    def is_valid(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        return not grid[x][y] # 0 => False, 1 =>True, but we want 0
                    
                        
                        
                        
                         

        
        
        
    