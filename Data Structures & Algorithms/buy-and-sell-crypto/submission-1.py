class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        left=0

        # window=[prices[0]]
        min_price=prices[0]
        max_profit=0
        for right in range(1,n):
            if prices[right]>min_price:
               
                max_profit=max(max_profit,prices[right]-min_price)
            else:
                min_price=prices[right]
                left=right
        return max_profit
        