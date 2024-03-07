from collections import deque

# directions = [(0,1),(0,-1),(1,0),(-1,0)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        max_area = 0
        visited = set()
        m, n = len(grid), len(grid[0]) # row, col

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = self.bfs(grid, visited, i, j)
                    max_area = max(max_area, area)

        return max_area
                    
    def bfs(self, grid, visited, x, y):
        queue = deque([(x,y)])
        visited.add((x,y))
        area = 0 

        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in directions:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
            
            area += 1 

        return area
                    
    def is_valid(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0]) # row, col
        if x >= m or x < 0 or y >= n or y < 0:
            return False
        if (x,y) in visited:
            return False
        return grid[x][y] == 1













































    #     if not grid or not grid[0]:
    #         return -1
    #     max_area = 0
    #     visited = set()

    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == 1 and (i,j) not in visited:
    #                 area = self.bfs(grid, visited, i, j)
    #                 max_area = max(max_area, area)
    #     return max_area


    # def bfs(self, grid, visited, x, y):
    #     queue = deque([(x, y)])
    #     visited.add((x, y))
    #     area = 0

    #     while queue:
    #         x, y = queue.popleft()
    #         for delta_x, delta_y in directions:
    #             next_x = x + delta_x
    #             next_y = y + delta_y
    #             if not self.is_valid(grid, next_x, next_y, visited):
    #                 continue
    #             queue.append((next_x,next_y))
    #             visited.add((next_x,next_y))
    #         area += 1
    #     return area

    # def is_valid(self, grid, x, y, visited):
    #     m, n = len(grid),len(grid[0])
    #     # print('grid[0][2] {}'.format(grid[0][2]))
    #     # print("m is {}, n is {}".format(m,n))
    #     if x < 0 or x >= m or y < 0 or y >= n:
    #         return False
    #     if (x, y) in visited:
    #         return False 
    #     return grid[x][y] == 1

        



            

   