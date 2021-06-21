class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        # left = bisect_left(arr, x) - 1
        # right = left + 1
        start, end = 0, len(arr)-1
        while start + 1 < end: 
            mid = (start + end) //2
            if arr[mid] >= x:
                end = mid
            else:
                start = mid 
        
        left, right = start, end 
        
        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]