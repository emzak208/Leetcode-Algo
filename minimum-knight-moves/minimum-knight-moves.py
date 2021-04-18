from collections import deque

directions = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        distance = {(0, 0): 0}
        queue = deque([(0, 0)])
        # visited = set()
        
        while queue:
            i, j = queue.popleft()
            if (i, j) == (x, y):
                return distance[(i, j)]
            for delta_x, delta_y in directions: 
                next_x = i + delta_x
                next_y = j + delta_y
                if (next_x,next_y) in distance:
                    continue 
                # if (next_x, next_y) not in visited:
                    # visited.add((next_x,next_y))
                distance[(next_x,next_y)] = distance[(i,j)] + 1 
                queue.append((next_x,next_y))

        
                
            