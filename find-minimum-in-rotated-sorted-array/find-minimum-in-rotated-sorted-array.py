class Solution:
    def findMin(self, nums: List[int]) -> int:
#         if not nums: 
#             return -1 
        
#         start, end = 0, len(nums) - 1 
#         while start + 1 < end:
#             mid = (start + end) // 2
#             if nums[mid] > end: 
#                 start = mid 
#             else: 
#                 end = mid 
#         return min(nums[start], nums[end])
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])