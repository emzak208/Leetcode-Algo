class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) # 5, 5
        if m == 0 or n == 0:
            return False 
        
        # 从左下角开始搜
        x, y = m - 1, 0 # 第m-1行，第0列
        while x >= 0 and y < n: # 当不出边界
            if matrix[x][y] == target: 
                return True 
            elif matrix[x][y] < target: # 如果<target，就往右搜
                y += 1 
            else: # 如果>target，就往上搜
                x -= 1 
                
        return False 
                
        
        