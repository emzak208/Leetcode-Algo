class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: 
            return -1 
        
        start, end = 0, len(nums) - 1
        while start + 1 < end: # 当start, end中间隔一个
            mid = (start + end) //2
            if nums[mid] < target: 
                start = mid 
            else: 
                end = mid 
                
        if nums[start] == target: 
            return start 
        elif nums[end] == target:
            return end 
        else:
            return -1 
        