class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        k = (n1 + n2 + 1) // 2
        
        if n1 > n2: 
            return self.findMedianSortedArrays(nums2, nums1)
        
        left = 0
        right = n1
        
        while left < right:
            m1 = (left + right) // 2 
            m2 = k - m1 
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1 
            else: 
                right = m1 
                
        m1 = left 
        m2 = k - left 
        # if m1 <= 0: 
        #     c1 = max(nums1[m1 - 1], nums2[m2 - 1])
            
        # 没有取m1中的元素
        c1 = max(
            float('-inf') if m1 <= 0 else nums1[m1 - 1],
            float('-inf') if m2 <= 0 else nums2[m2 - 1]
        )
        
        if (n1 + n2) % 2 == 1:
            return c1
        
        c2 = min(
            float('inf') if m1 >= n1 else nums1[m1],
            float('inf') if m2 >= n2 else nums2[m2]
        )
        
        return (c1 + c2) / 2
            
            
                
            