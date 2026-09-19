class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min1 = prices[0]
        for price in prices:
            if price < min1:
                min1 = price
            if price - min1 > profit:
                profit = price - min1
        return profit