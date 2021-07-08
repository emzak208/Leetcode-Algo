class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False 

        nrow, ncol = len(matrix), len(matrix[0])
        start, end = 0, nrow * ncol - 1

        while start + 1 < end:
            mid = (start + end) // 2
            x, y = mid // ncol, mid % ncol # 把数列坐标还原成二位数组中的下标
            if matrix[x][y] < target:
                start = mid 
            else: 
                end = mid 

        x, y = start // ncol, start % ncol
        if matrix[x][y] == target:
            return True 

        x, y = end // ncol, end % ncol
        if matrix[x][y] == target:
            return True    