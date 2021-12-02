import sys
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    low = prices[0]
    for i in range(1, len(prices)):
        low = min(low, prices[i])
        profit = max(profit, prices[i]-low)
    return profit