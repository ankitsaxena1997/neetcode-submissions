class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit=0

        buy=0
        i=1

        while i<len(prices):
            
            if prices[i] > prices[buy]:
                profit=prices[i]-prices[buy]
                max_profit=max(profit,max_profit)
            else:
                buy=i
            
            i=i+1

        return max_profit
        