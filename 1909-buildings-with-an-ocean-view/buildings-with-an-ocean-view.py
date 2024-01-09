class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Optimized method 1 iterates only once, O(n)
        res = []

        for curr in range(len(heights)):
            while res and heights[res[-1]] <= heights[curr]:
                res.pop()
            res.append(curr)
    
        return res






        # # method 1 : brute force O(n^2) => TLE
        # res = []

        # for i in range(len(heights)):
        #     r = i + 1 
        #     while r < len(heights):
        #         if heights[r] < heights[i]:
        #             r += 1 
        #     if r == len(heights) - 1:
        #         res.append[i]
        
        # return res

                    



