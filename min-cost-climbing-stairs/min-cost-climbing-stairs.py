class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0 for i in range(len(cost)+1)]
        memo[0] = 0
        memo[1] = cost[0]
        
        for i in range(2,len(memo)):
            memo[i] = cost[i-1] + min(memo[i-1],memo[i-2])
        
        return min(memo[-1],memo[-2])