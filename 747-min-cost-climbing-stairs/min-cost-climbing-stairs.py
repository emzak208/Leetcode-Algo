class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2]) # or simplify as cost[i] = min(ccost[i + 1], cost[i + 2])

        return min(cost[0], cost[1]) # starting from either index 0 or 1 and take min
            



        