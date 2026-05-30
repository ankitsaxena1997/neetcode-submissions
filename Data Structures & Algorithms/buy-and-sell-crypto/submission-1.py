class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit=0

        buy=0
        sell=0
        i=1

        while i<len(prices):
            
            if prices[i] > prices[buy]:
                sell=i
                profit=prices[i]-prices[buy]
                max_profit=max(profit,max_profit)
            else:
                sell=i
                buy=i
            
            i=i+1

        return max_profit
        