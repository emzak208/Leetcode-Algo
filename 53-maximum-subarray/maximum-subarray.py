class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

    # Method 1: bruteforce O(n^2)    
        # max_subarray = -math.inf

        # for i in range(len(nums)):
        #     curr_subarray = 0
        #     for j in range(i, len(nums)):
        #         curr_subarray += nums[j]
        #         max_subarray = max(max_subarray, curr_subarray)

        # return max_subarray        

    # Method 2: dymanic programming 
        curSub = 0
        maxSub = -math.inf

        for n in nums:
            if curSub < 0:
                curSub = 0
            curSub += n
            maxSub = max(curSub, maxSub)

        return maxSub