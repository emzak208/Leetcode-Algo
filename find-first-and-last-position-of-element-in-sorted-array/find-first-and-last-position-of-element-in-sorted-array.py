class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return -1, -1 
        
        # first position 
        start, end = 0, len(nums) - 1
        while start + 1 < end: 
            mid = (start + end) // 2
            if nums[mid] < target: 
                start = mid 
            else: # 当寻找第一次出现的位置，我们选择左区间去找， 所以等于的情况放在有区间，即else 里
                end = mid 
        
        if nums[start] == target:# 找第一次出现，所以先判断start 
            left_bound = start 
        elif nums[end] == target:
            left_bound = end
        else: 
            left_bound = -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end: 
            mid = (start + end) // 2
            if nums[mid] <= target: # 找最后一次出现的数，所以锁定右区间去找， 即把等于的放在右区间
                start = mid 
            else: 
                end = mid 
                
        if nums[end] == target: # 找最后一次出现，所以先判断end 
            right_bound = end 
        elif nums[start] == target: 
            right_bound = start 
        else: 
            right_bound = -1 
            
        return [left_bound,right_bound]
            
            