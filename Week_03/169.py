class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #股票交易，不限次数
        if len(prices)==0 :
            return 0
        dp = [[0 for i in range(2)] for i  in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][1]+prices[i],dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]-prices[i],dp[i-1][1])
        return dp[-1][0]