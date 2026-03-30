class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        f=1
        profit=0
        n=len(prices)
        while f<n:
            if prices[s]<prices[f]:
                profit = max(profit,prices[f]-prices[s])
            else:
                s=f
            f+=1
        return profit
