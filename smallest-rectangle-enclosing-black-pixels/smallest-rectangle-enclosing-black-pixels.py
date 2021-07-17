class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0]) # row, col 
        if m == 0 or n == 0:
            return 0
        
        # 二分最左侧黑像素位置
        l, r = 0, y
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check_column(image, mid):
                r = mid
            else:
                l = mid
        if self.check_column(image, l):
            left = l
        else:
            left = r
            
        # 二分最右侧黑像素位置
        l, r = y, n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check_column(image, mid):
                l = mid
            else:
                r = mid
        if self.check_column(image, r):
            right = r
        else:
            right = l
            
            
        #  二分最上面黑像素位置
        l, r = 0, x
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check_row(image,left, right, mid):
                r = mid
            else:
                l = mid
        if self.check_row(image, left, right, l):
            top = l
        else:
            top = r
            
        # 二分最下面黑像素位置
        l, r = x, m - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check_row(image, left, right, mid):
                l = mid
            else:
                r = mid 
        if self.check_row(image, left, right, r):
            buttom = r
        else:
            buttom = l
            
        return (right - left + 1) * (buttom - top + 1)
    
    ## 2 helper functions: 
    # 判断左右边界时 check column 
    def check_column(self, image, col):# 判断列里的每个数是不是等于1
        for i in range(len(image)):
            if image[i][col] == "1":
                return True
        return False 
    
    # 当左右边界确定，需要确定上下边界时，只需要在左右边界所在的列中查看每行是否右1，可以减少搜索面积
    def check_row(self, image, left, right, row):
        for j in range(left, right + 1): # right是位置， 因为range不包括边界，所以要+1才能cover到right 
            if image[row][j] == "1":
                return True
        return False 
            
        
        
        