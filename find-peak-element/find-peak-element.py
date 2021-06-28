class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums: 
            return -1 
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid 
            elif nums[mid] < nums[mid - 1]: 
                end = mid 
            else: # nums[mid] < nums[mid + 1]:
                start = mid 
         
        if nums[start] < nums[end]:
            return end
        else: 
            return start 

                
        