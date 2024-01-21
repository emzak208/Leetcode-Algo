class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # method 1: bruce force O(n^2) 
        # cnt = 0 

        # for i in range(len(nums)): # 0,1,2
        #     summ = 0
        #     for j in range(i, len(nums)): # i -> 2
        #         summ += nums[j]
        #         if summ == k:
        #             cnt += 1
        # return cnt

        # [1,2,3]
        cnt = 0 
        cum_sum = 0
        prefix_sum = {0: 1}

        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum - k in prefix_sum:
                cnt += prefix_sum[cum_sum - k]
            if cum_sum in prefix_sum:
                prefix_sum[cum_sum] += 1 
            else:
                prefix_sum[cum_sum] = 1
        return cnt

            
            


        