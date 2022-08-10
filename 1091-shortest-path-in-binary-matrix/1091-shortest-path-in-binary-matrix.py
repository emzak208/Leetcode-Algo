from collections import deque 
# directions = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
directions = [(1,0),(0,1),(-1,0),(0,-1), (1,1),(1,-1),(-1,1),(-1,-1)]

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        distance = {(0,0):1} # initial distance = 1 
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        queue = deque([(0,0)])
        while queue: 
            x, y = queue.popleft()
            if (x, y) == (max_row,max_col):
                return distance[(x,y)] 
            for (delta_x, delta_y) in directions:
                next_x = x + delta_x
                next_y = y + delta_y
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(grid, next_x, next_y):
                    continue
                distance[(next_x,next_y)] = distance[(x,y)] + 1
                queue.append((next_x,next_y))
                
        return -1
    
    def is_valid(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return False 
        return not grid[x][y]
            
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         distance = {(0,0): 1}
#         max_row = len(grid) - 1
#         max_col = len(grid[0]) - 1
        
#         # if start | end == 1, can't find a path 
#         if grid[0][0] != 0 or grid[max_row][max_col] != 0:
#             return -1 
        
#         # bfs
#         queue = deque([(0, 0)])
        
#         while queue: 
#             x, y = queue.popleft()
#             if (x, y) == (max_row, max_col): # if already the last, return distance
#                 return distance[(x ,y)]
#             for delta_x, delta_y in directions: 
#                 next_x = x + delta_x
#                 next_y = y + delta_y
#                 if (next_x, next_y) in distance: # avoid duolicate points 
#                     continue
#                 if not self.is_valid(next_x, next_y, grid): # only run bfs for point == 0
#                     continue 
#                 distance[(next_x, next_y)] = distance[(x, y)] + 1
#                 queue.append((next_x, next_y))
#         # print('Q exhausted')
#         return -1 # if can't reach the destination, eg 0 surcounded by 3 1's, then -1
    
#     def is_valid(self, x, y, grid):
#         m, n = len(grid), len(grid[0])
#         if x < 0 or x >= m or y < 0 or y >= n: # x, y can be 0
#             return False
#         return not grid[x][y] # 0 => False, 1 =>True, but we want 0
                    
                        
                        
                        
                         

        
        
        
    