class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        total = 0

        for num in w: 
            total += num
            self.prefix_sum.append(total)

        self.total = total
  
    def pickIndex(self) -> int:
        # w = [1,2,3,4,5]
        # long_version = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5] => len = 15 
        # prefix_sum = [1,3,6,10,15]

        target = random.uniform(0, self.total) # randomly pick a number from long_version
        l, r = 0, len(self.prefix_sum)

        while l < r: 
            mid = (l + r) // 2 

            if self.prefix_sum[mid] <= target:
                l = mid + 1
            else:
                r = mid 

        return l 


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()