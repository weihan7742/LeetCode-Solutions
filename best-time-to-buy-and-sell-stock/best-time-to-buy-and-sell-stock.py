class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        memo = [0 for _ in range(len(prices)+1)]
        memo[0] = 0

        minimum = float('inf')
        profit = 0

        for i in range(1,len(memo)):
            index = i-1
            memo[i] = prices[index]-minimum

            if memo[i] > profit:
                profit = memo[i]

            if prices[index] < minimum:
                minimum = prices[index]
    
        return profit